#!/usr/bin/python3
from web_flask import app
from flask import render_template, abort
from models import storage


@app.route('/states')
@app.route('/states/<id>')
def get_state(id=None):
    states_db = storage.all('State')
    states = {'size': 0, 'states': list()}
    if id:
        key = 'State.{}'.format(id)
        if key in states_db:
            states['states'].append(states_db.get(key))
            states['size'] = 1
        else:
            states = None
    else:
        for key, state in states_db.items():
            states['size'] += 1
            states['states'].append({
                'id': state.id,
                'name': state.name,
                })
    return render_template("9-states.html", item=states)

    
@app.teardown_appcontext
def teardown_storage(self):
    storage.close()

if __name__ == "__main__":
    app.run()
