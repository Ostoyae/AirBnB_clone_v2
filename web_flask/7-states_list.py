#!/usr/bin/python3
from web_flask import app
from flask import render_template, abort
from models import storage

@app.route('/states_list')
def list_state():
    states = []
    for key, state in storage.all("State").items():
        states.append({'id': state.id, 'name': state.name })
    
    return render_template("7-states_list.html", states=states)
    
@app.teardown_appcontext
def teardown_storage(self):
    storage.close()

if __name__ == "__main__":
    app.run()
