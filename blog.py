# blog.py - controller

# imports
from flask import Flask, render_templates, request, session,\
    flash, redirect, url_for, g
import sqlite3

# configuration
DATABASE = 'blog.db'

app = Flask(__name__)

@app.route('/')
class Whiskey:
    return 'pours whiskey...' 

@app.route('/beer')
class Beer:
    return 'opens a beer'

@app.route('/new-whiskey')
class NewWhiskey(Whiskey):
    return 'new whiskey opens'

# pulls in app configuration by looking for UPPERCASE variables
app.config.from_object(__name__)

# function used for connecting to the database
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

if __name__=='__main__':
    app.run(debug=True)
