from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

@app.route('/')
def home():
    """Returns Homepage"""
    return render_template('home.html')

@app.route('/profile')
def profile():
    """Returns profile"""
    return "hi"

if __name__ == '__main__':
    app.run(debug=True)
