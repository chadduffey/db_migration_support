import dropbox
import os

import scripts.dbcheck as dbcheck


TOKEN = os.environ['DB_TOKEN']
DEBUG = True


if __name__ == "__main__":

	dbx = dropbox.Dropbox(TOKEN)
	connection_result = dbcheck.check(dbx)

