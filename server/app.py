#!/usr/bin/env python3

from flask import Flask, make_response, request
from flask_migrate import Migrate


from models import db, Zookeeper, Enclosure, Animal

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return '<h1>Zoo app</h1>'


@app.route('/animal/<int:id>')
def animal_by_id(id):

    animal = Animal.query.filter(Animal.id == id).first()
    animal_dict = {
        'id': animal.id,
        'species': animal.species,
        'name': animal.name,
        'zookeeper': animal.zookeeper_id,
        'enclosure': animal.enclosure_id
    }
    response = make_response(animal_dict, 200)
    return response

@app.route('/zookeeper/<int:id>')
def zookeeper_by_id(id):
    zookeeper = Zookeeper.query.filter(Zookeeper.id == id).first()
    zookeeper_dict = {
        'id': zookeeper.id,
        'birthday': zookeeper.birthday,
        'name': zookeeper.name,
    }
    response = make_response(zookeeper_dict, 200)
    return response

@app.route('/enclosure/<int:id>')
def enclosure_by_id(id):
    enclosure = Enclosure.query.filter(Enclosure.id == id).first()
    enclosure_dict = {
        'id': enclosure.id,
        'envirnoment': enclosure.environment,
        'open_to_visitors': enclosure.open_to_visitors,
    }
    response = make_response(enclosure_dict, 200)
    return response

if __name__ == '__main__':
    app.run(port=5555, debug=True)
