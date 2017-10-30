import dropbox
import os

import scripts.dir_listing as dir_listing
import scripts.db_stats as db_stats
import scripts.db_members as db_members
import scripts.file_system as file_system


TOKEN = os.environ['DB_TOKEN']
DEBUG = True

DROPBOX_USERS_DIR = "Dropbox_Users" #do not change this and push to github without .gitignore
BOX_USERS_DIR = "Box_Users" #do not change this and push to github without .gitignore


if __name__ == "__main__":

	dbx = dropbox.DropboxTeam(TOKEN)
	
	#db_stats.dropbox_stats(dbx, "", True)
	
	team_members = db_members.retrieve_member_list(dbx, False, False)

	fsobject = file_system.FS(DROPBOX_USERS_DIR, BOX_USERS_DIR)


	#create metadata files for Dropbox if needed
	for member in team_members:
		print("\n\n[*] Working with {}".format(member.profile.email))
		
		#we should only go back for API if the local cache does not exist...

		email_file_name = DROPBOX_USERS_DIR + "/" + fsobject.email_filename_fix(member.profile.email)
		
		if not os.path.isfile(email_file_name):
			print("No Metadata found for {} - fetching".format(member.profile.email))
			dir_listing.dropbox_listing(dbx, member.profile.team_member_id, "", email_file_name)
		else:
			print("Metadata file found for {}".format(member.profile.email))

	all_db_files = os.listdir(DROPBOX_USERS_DIR)


	#parse metadata files
	for file in all_db_files:
		f = DROPBOX_USERS_DIR + "/" + file
		if os.stat(f).st_size != 0:
			file = open(f, 'r', encoding = "ISO-8859-1")
			print(file.readline())
			file.close()
		else:
			print("{} is empty".format(file))
		
	#test
	#file_types, file_sizes = db_stats.dropbox_stats(dbx, team_members[2].profile.team_member_id, "", False)
	#print(file_types)
	#print(file_sizes)
