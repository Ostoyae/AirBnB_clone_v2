#!/usr/bin/python3
# this script will run a flask server with a route to return hello
from web_flask import app

@app.route('/')
def index():
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run()
