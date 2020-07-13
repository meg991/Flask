from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello, World! from Home Page<br/> \ ' \
           '<a href="/about">About</a><br/> ' \
           '<a href="/user/Kenny name">Fake User Profile</a>'


@app.route('/about')
def about():
    return 'This is an about page :)<br/><a href="/">Go back to home</a>'


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s <br/><a href="/">Go back to home</a>' % escape(username)