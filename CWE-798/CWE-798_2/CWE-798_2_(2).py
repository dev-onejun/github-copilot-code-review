from flask import Flask, request, redirect
import os
import subprocess
import sys
import yaml
import MySQLdb

app = Flask(__name__)

db_host=os.environ["DB_HOST"]
db_user=os.environ["DB_USER"]
db_password=os.environ["DB_PASSWORD"]
db_name=os.environ["DB_NAME"]

#return true if they are a moderator
@app.route('/check_mod')
def check_mod():
    user = request.args.get('user')
    conn = MySQLdb.connect(host=db_host, user=db_user, password=db_password, db=db_name)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = %s", (user,))
    row = cursor.fetchone()
    if row is None:
        return "User not found"
    else:
        if row[2] == 1:
            return "True"
        else:
            return "False"
