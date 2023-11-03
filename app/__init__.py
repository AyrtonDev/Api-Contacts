from flask import Flask, make_response, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://root:root@localhost:5432/mycontacts'
db = SQLAlchemy(app)

@app.route('/ping')
def ping():
    return make_response(jsonify({'pong': True}))

from app import routes

@app.errorhandler(500)
def error_internal():
    return make_response(jsonify({'error': 'Internal error'}), 500)

# TODO: create the documentation
# TODO: create the tests
# TODO: create the docker file
