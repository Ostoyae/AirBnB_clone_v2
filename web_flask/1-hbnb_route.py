#!/usr/bin/python3
# add route '/hbnb' returns HBNB
from web_flask import app


@app.route('/')
def index():
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    return 'HBNB'


if __name__ == '__main__':
    app.run()
