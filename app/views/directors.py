from flask_restx import Resource, Namespace
from flask import request, jsonify
from app.schemas import *
from app.models import *
from app.functions import set_keys

directors_ns = Namespace('directors')
director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)

@directors_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        all_directors = Director.query.all()
        return jsonify(directors_schema.dump(all_directors))

    def post(self):
        req_json = request.json
        new_director = Director(**req_json)
        with db.session.begin():
            db.session.add(new_director)
        return "", 201


@directors_ns.route('/<int:uid>')
class DirectorView(Resource):
    def get(self, uid):
        director = Director.query.get(uid)
        return jsonify(director_schema.dump(director))

    def put(self, uid: int):
        note = Director.query.get(uid)
        req_json = request.json
        set_keys(req_json, note)
        db.session.add(note)
        db.session.commit()
        return "", 204

    def delete(self, uid: int):
        director = Director.query.get(uid)
        db.session.delete(director)
        db.session.commit()