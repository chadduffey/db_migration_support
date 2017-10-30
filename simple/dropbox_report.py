import collections
import multiprocessing

import dropbox
import os

import library

TOKEN = os.environ['DB_TOKEN']
USERS_DIR = "users/"

dbx = dropbox.DropboxTeam(TOKEN)

def _write_member_file(member, listing):

	f = open(USERS_DIR + member.profile.email, 'w')

	for item in listing:
		f.write(item)

	f.close()


def process_member(member):

	print("Processing {}".format(member.profile.email))
	if os.path.exists(USERS_DIR + member.profile.email):
		print("\tmetafile for {} already exists.".format(member.profile.email))
		return {
				'id': member.profile.email,
				'content' : 'no_change'
			}

	listing = library.dropbox_listing(dbx, member.profile.team_member_id, "")
	_write_member_file(member, listing)
	print("\tCompleted {}, {} items located".format(member.profile.email, len(listing)))
	
	return {
			'id': member.profile.email,
			'content' : listing
		}


if __name__ == "__main__":

	print("Retrieving members")
	members = library.retrieve_member_list(dbx, recursive=False, debug=False)
	print("{} Members Retrieved.".format(len(members)))

	print(process_member(members[0]))
		
	pool = multiprocessing.Pool()
	result = pool.map(process_member, members)

	print(result) 

	