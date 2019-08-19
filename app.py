"""Simple bookstore Flask app."""

from flask import Flask, request, redirect, render_template, flash
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"

toolbar = DebugToolbarExtension(app)

@app.route('/')
def welcome_message():
    return render_template('base.html')
