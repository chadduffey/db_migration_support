#Dropbox metadata object, one should be constructed for each local metadata file. 

import os

class DB_Metadata(object):

	def __init__(self, file_path):

		#should take email as parameter
		#find the file
		#if not exist, set a flag on the object so that we can come back to get it. 
		#if exist, offer up some interfaces (similar to api) for working with the object. 
		#the benefit here is speed. at least 10 times faster to parse local object. 

		if os.path.isfile(file_path):
			print("Located metadata for user at {}".format(file_path))
		else:
			print("No metadata file found for user at {}".format(file_path))
			return False

		


