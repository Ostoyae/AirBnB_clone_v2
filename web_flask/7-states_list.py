#!/usr/bin/python3
from flask import Flask
from flask import abort, render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def list_state():
    '''Get states form DB and renders a
    list of all the state with their id
    '''
    states = []
    for key, state in storage.all("State").items():
        states.append({'id': state.id, 'name': state.name})
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown_storage(self):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0')
