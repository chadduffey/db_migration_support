import collections
import concurrent.futures

import dropbox
import os
import time

import library

TOKEN = os.environ['DB_TOKEN']
USERS_DIR = "users/"

dbx = dropbox.DropboxTeam(TOKEN)

def _write_member_file(member, listing):

	f = open(USERS_DIR + member.profile.email, 'w')

	for item in listing:
		f.write(item + "\n")

	f.close()


def process_member(member):

	print("Process {} working on {}".format(os.getpid(), member.profile.email))
	
	#Dont process members who we already have metadata for:
	if os.path.exists(USERS_DIR + member.profile.email):
		print("\tmetafile for {} already exists.".format(member.profile.email))
		return {
				'id': member.profile.email,
				'content' : 'no_change'
			}

	#process member:
	listing = library.dropbox_listing(dbx, member.profile.team_member_id, "")
	_write_member_file(member, listing)
	print("\tCompleted {}, {} items located".format(member.profile.email, len(listing)))
	
	#return a dictionary for the member to the multithreaded handler. 
	return {
			'id': member.profile.email,
			'content' : listing
		}


if __name__ == "__main__":

	#retrieve members
	start = time.time()
	print("Retrieving members")
	members = library.retrieve_member_list(dbx, recursive=True, debug=False)
	end = time.time()
	print("{} Members Retrieved in {} seconds".format(len(members), end - start))

	#parrellel process calls into process member:		
	start = time.time()
	with concurrent.futures.ProcessPoolExecutor() as executor:
		result = executor.map(process_member, members)
	end = time.time()
	print("Processed members in {} seconds".format(end - start))


	