#!/usr/bin/env python3
"""

"""
from flask import Babel
from flask import request
from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/')
def hello_world():
    """
    
    """
    return render_template('0-index.html')

if __name___ == "__main__":
    app.run(host="0.0.0.0", port="5000")
