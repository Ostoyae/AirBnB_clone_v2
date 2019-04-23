#!/usr/bin/python3
from flask import Flask
from flask import abort, render_template
from flask import render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/hbnb_filters')
def get_hbnb_filters():
    ''' fetches states and amenities form DB 
    then renders the template
    '''
    states = storage.all("State")
    amenity = storage.all("Amenity")
    return render_template(
        '10-hbnb_filters.html',
        states=states,
        amenities=amenity
    )


if __name__ == '__main__':
    app.run()
