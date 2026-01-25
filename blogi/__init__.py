from flask import Flask
from flask import render_template, request, redirect
from werkzeug.security import generate_password_hash

import sqlite3

from . import db

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/authors/")
def authors():
    return render_template("authors.html")

@app.route("/tags/")
def tags():
    return render_template("tags.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/register", methods=["POST"])
def register_post():
    username = request.form["username"]
    password1 = request.form["password1"]
    password2 = request.form["password2"]
    if password1 != password2:
        return "the passwords did not match"

    password_hash = generate_password_hash(password1)

    try:
        query = "INSERT INTO users (username, password_hash) VALUES (?, ?)"
        db.execute(query, [username, password_hash])
    except sqlite3.IntegrityError:
        return "the username is taken"

    return redirect("/login")
