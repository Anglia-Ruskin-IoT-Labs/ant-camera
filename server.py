#!/usr/bin/python3

from flask import Flask, send_file, make_response
from flask_cors import CORS
#from functools import wraps, update_wrapper
#from datetime import datetime

flask = Flask(__name__)
CORS(flask)

@flask.route('/getTemp', methods=['GET'])
def sensor():
    
    return send_file('reading.txt')

@flask.after_request

def add_header(r):
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

flask.run('0.0.0.0', '8080', threaded=True, debug=True)
