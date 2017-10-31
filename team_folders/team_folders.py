import dropbox
import os

TOKEN = os.environ['DB_TOKEN']

dbx = dropbox.DropboxTeam(TOKEN)

if __name__ == "__main__":

	team_folders = dbx.team_team_folder_list()

	for folder in team_folders.team_folders:
		print(folder)

	print("\nNumber of team folders: {}".format(len(team_folders.team_folders)))