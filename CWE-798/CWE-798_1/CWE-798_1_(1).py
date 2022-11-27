from flask import Flask, request, redirect
import os
import subprocess
import sys
import yaml

app = Flask(__name__)

# return true if they are a moderator
@app.route('/check_mod')
def check_mod():
    if request.args.get('username') == 'admin':
        return 'true'
    else:
        return 'false'
