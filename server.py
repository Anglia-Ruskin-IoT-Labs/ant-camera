#!/usr/bin/python3

#import libraries
from flask import Flask, send_file, make_response
from flask_cors import CORS

#create Flask server
flask = Flask(__name__)
CORS(flask)


@flask.route('/getTemp', methods=['GET'])
def sensor():
    
    return send_file('reading.txt')

@flask.after_request

#clear cache
def add_header(r):
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

#strart Flask server
flask.run('0.0.0.0', '8080', threaded=True, debug=True)
