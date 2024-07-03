# main.py

from flask import Flask, render_template, url_for, flash, redirect, request
import git

app = Flask(__name__)

@app.route("/update_server", methods=['POST'])
def webhook():
    if request.method == 'POST':
        repo = git.Repo('/home/crave/craveweb')
        origin = repo.remotes.origin
        origin.pull()
        return 'Updated PythonAnywhere successfully', 200
    else:
        return 'Wrong event type', 400
