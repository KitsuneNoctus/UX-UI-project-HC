from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

@app.route('/')
def home():
    """Returns Homepage"""
    return render_template('home.html', message = "hello word")

@app.route('/profile')
def profile():
    """Returns profile"""
    return render_template('profile.html')

@app.route('/chatrooms')
def chatrooms():
    """Shows all the Chatrooms avaiable"""
    return render_template('chatroom_menu.html')

@app.route('/chatroom')
def chatroom():
    """Example chatroom"""
    return render_template('example_chatroom.html')

if __name__ == '__main__':
    app.run(debug=True)
