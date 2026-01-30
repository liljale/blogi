from flask import Flask
from flask import render_template, request, redirect, session, flash
from werkzeug.security import generate_password_hash, check_password_hash

import sqlite3

from . import db
from . import config

app = Flask(__name__)
app.secret_key = config.secret_key

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

@app.route("/login", methods=["POST"])
def login_post():
  error = None
  username = request.form["username"]
  password = request.form["password"]

  password_hash = db.get_password_hash(username)

  if password_hash is None:
    error = "invalid username or password"
  else:
    if check_password_hash(password_hash[0], password):
      session["username"] = username
      flash("login successful")
      return redirect("/")
    else:
      error = "invalid username or password"

  return render_template("login.html", error=error)

@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")

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
