#!/usr/bin/env python3

from flask import Flask, make_response, jsonify
from flask_migrate import Migrate

from .models import db, Zookeeper, Enclosure, Animal

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def home():
    return '<h1>Zoo app</h1>'

@app.route('/animal/<int:id>')
def animal_by_id(id):
    animal = Animal.query.get(id)
    if animal:
        # Create a dictionary to represent the animal's data
        animal_data = {
            'Name': animal.name,
            'Species': animal.species,
            'Zookeeper': animal.zookeeper.name if animal.zookeeper else None,
            'Enclosure': animal.enclosure.name if animal.enclosure else None,
        }
        return jsonify(animal_data)
    else:
        # Return a 404 response if the animal with the given ID is not found
        return make_response(jsonify({'error': 'Animal not found'}), 404)

@app.route('/zookeeper/<int:id>')
def zookeeper_by_id(id):
    zookeeper = Zookeeper.query.get(id)
    if zookeeper:
        # Create a dictionary to represent the zookeeper's data
        zookeeper_data = {
            'Name': zookeeper.name,
            'Birthday': str(zookeeper.birthday),
            'Animals': [animal.name for animal in zookeeper.animals],
        }
        return jsonify(zookeeper_data)
    else:
        # Return a 404 response if the zookeeper with the given ID is not found
        return make_response(jsonify({'error': 'Zookeeper not found'}), 404)

@app.route('/enclosure/<int:id>')
def enclosure_by_id(id):
    enclosure = Enclosure.query.get(id)
    if enclosure:
        # Create a dictionary to represent the enclosure's data
        enclosure_data = {
            'Environment': enclosure.environment,
            'Open to Visitors': enclosure.open_to_visitors,
            'Animals': [animal.name for animal in enclosure.animals],
        }
        return jsonify(enclosure_data)
    else:
        # Return a 404 response if the enclosure with the given ID is not found
        return make_response(jsonify({'error': 'Enclosure not found'}), 404)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
