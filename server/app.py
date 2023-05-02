#!/usr/bin/env python3

# Standard library imports
import os

# Remote library imports
from flask import Flask, jsonify, make_response, request, session, abort
from flask_restful import Resource, Api
from flask_migrate import Migrate
from werkzeug.exceptions import NotFound, Unauthorized

# Local imports
from models import db, Athlete

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

def __init__(self):
    pass

api = Api(app)

# Views go here!

class Athletes(Resource):
    def get(self):
        athlete = [athlete.to_dict() for athlete in Athlete.query.all()]
        return make_response(jsonify(athlete), 200)
    
api.add_resource(Athletes, '/athletes')

if __name__ == '__main__':
    app.run(port=5555, debug=True)
