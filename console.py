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

	#dbx = dropbox.DropboxTeam(TOKEN)
	
	#db_stats.dropbox_stats(dbx, "", True)
	
	#team_members = db_members.retrieve_member_list(dbx, False, False)

	#test - max 10 users
	'''
	count = 0
	for member in team_members:
		print("\n\n{}".format(member.profile.email))
		dir_listing.dropbox_listing(dbx, member.profile.team_member_id, "", testing_mode=True)
		if count >= 10:
			break
		
		count = count + 1
	'''

	#test
	#file_types, file_sizes = db_stats.dropbox_stats(dbx, team_members[2].profile.team_member_id, "", False)
	#print(file_types)
	#print(file_sizes)

	fsobject = file_system.FS(DROPBOX_USERS_DIR, BOX_USERS_DIR)
	fsobject.create_dropbox_metafile("test@test.com")

