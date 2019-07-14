from flask import Flask, jsonify
from flask import render_template, request
from datetime import datetime
import time
import json

import data

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/test')
def test():
    return "Geolocation tracking works ..."

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True, debug=True)
