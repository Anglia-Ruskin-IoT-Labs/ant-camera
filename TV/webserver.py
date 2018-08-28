#!env/bin/python3
from flask import Flask, render_template

server = Flask(__name__)



@server.route('/')
def index():
	return render_template('index.html')




server.run(host='127.0.0.1', port=8080, threaded=True, debug=True)
