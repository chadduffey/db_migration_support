import dropbox
import json

def dropbox_listing(dbx, user_id, path, out_filename):

	
	listing = []  
	print(listing)

	try:
		dir_listing = dbx.as_user(user_id).files_list_folder(path)

		#fix paging... must go past 1000...

		for item in dir_listing.entries:
			
			if type(item) == dropbox.files.FileMetadata: 
				print(". {}".format(item.name))
				listing.extend(item.name)

			if type(item) == dropbox.files.FolderMetadata: 
				print("{}".format(item.path_display))
				listing.extend(item.name)

				dropbox_listing(dbx, user_id, item.path_display, out_filename)

	except:		
		if path == "":
			path = "{folder root}"
		
		print("[!] Failed to return path {}".format(path))

	

	return listing