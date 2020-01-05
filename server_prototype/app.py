#!/usr/bin/env python
from flask import Flask

app = Flask(__name__)

# Hello world prototype responce.
@app.route('/')
def index():
    return "Hello, World!"

# Route that echos out last part of path.
@app.route('/api/echo/<string:v>', methods=['GET'])
def get_tasks(v):
    return v


if __name__ == '__main__':
    app.run(debug=True)
