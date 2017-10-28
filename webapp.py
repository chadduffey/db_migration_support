import dropbox
import os

import scripts.dbcheck as dbcheck

from flask import Flask, render_template 

TOKEN = os.environ['DB_TOKEN']
DEBUG = True

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = DEBUG


@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html',
                           title='Home',
                           connection_result=connection_result)	


if __name__ == "__main__":

	dbx = dropbox.Dropbox(TOKEN)
	connection_result = dbcheck.check(dbx)

	app.run()