#!/usr/bin/python3
from web_flask import app
from models import storage
from flask import render_template

@app.route('/hbnb_filters')
def get_hbnb_filters():
    states = storage.all("State")
    amenity = storage.all("Amenity")
    return render_template(
            '10-hbnb_filters.html',
            states=states,
            amenities=amenity
            )


if __name__ == '__main__':
    app.run()
