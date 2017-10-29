import dropbox
import json

def dropbox_listing(dbx, user_id, path, out_filename, file=None):

	if not file:
		file = open(out_filename, 'w')

	try:
		dir_listing = dbx.as_user(user_id).files_list_folder(path)

		#fix paging... must go past 1000...

		for item in dir_listing.entries:
			
			if type(item) == dropbox.files.FileMetadata: 
				print(". {}".format(item.name))				
				file.write(str(item) + "\n")

			if type(item) == dropbox.files.FolderMetadata: 
				print("{}".format(item.path_display))
				file.write(str(item) + "\n")

				dropbox_listing(dbx, user_id, item.path_display, out_filename)

	except:		
		if path == "":
			path = "{folder root}"
		
		print("[!] Failed to return path {}".format(path))

	file.close()

	#return listing