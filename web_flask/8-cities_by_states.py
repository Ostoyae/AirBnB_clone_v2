#!/usr/bin/python3
from flask import Flask
from flask import abort, render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def list_state():
    states = []
    for key, state in storage.all("State").items():
        states.append({
            'id': state.id,
            'name': state.name,
        })

    return render_template("7-states_list.html", states=states)


@app.route('/cities_by_state')
def cities_by_state():
    ''' Gets State from DB and renders
    template that displays state and their cities
    '''
    states = []
    for key, state in storage.all("State").items():
        states.append({
            'id': state.id,
            'name': state.name,
            'cities': state.cities
        })

    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown_storage(self):
    ''' Teardown storage
    '''
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0')
