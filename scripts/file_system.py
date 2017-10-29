#set up and interact with the local caching system.

import os


class FS(object):

	def __init__(self, db_folder, box_folder):

		if os.path.isdir(db_folder):
			print("[*] Dropbox Folder Exists")
		else:
			os.mkdir(db_folder)
			print("[*] Created Dropbox Folder")

		if os.path.isdir(box_folder):
			print("[*] Box Folder Exists")
		else:
			os.mkdir(box_folder)
			print("[*] Created Box Folder")

		self.box_folder = box_folder
		self.db_folder = db_folder

	def email_filename_fix(self, email):
		return email.replace("@", "_at_")

	def box_folder_exists(self):
		return os.path.isdir(box_folder)


	def dropbox_folder_exists(self):
		return os.path.isdir(db_folder)


	def create_box_metafile(self):
		pass


