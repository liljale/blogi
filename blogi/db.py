import sqlite3

DATABASE= 'database.db'

def get_connection():
    con = sqlite3.connect(DATABASE)
    con.row_factory = sqlite3.Row
    return con

def execute(query, args=(),one=False):
    con = get_connection()
    con.execute(query, args)
    con.commit()
    con.close()

def query(query, args=(), one=False):
    con = get_connection()
    result = con.execute(query, args).fetchall()
    con.close()
    return result

def get_password_hash(user):
    con = get_connection()
    query = "SELECT password_hash FROM users WHERE username = ?"
    result = con.execute(query, [user]).fetchone()
    con.close
    return result
