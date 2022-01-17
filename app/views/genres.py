from flask_restx import Resource, Namespace
from flask import request, jsonify
from app.schemas import *
from app.models import *
from app.functions import set_keys

genres_ns = Namespace('genres')
genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)

@genres_ns.route('/')
class GenresView(Resource):
    def get(self):
        all_genres = Genre.query.all()
        return jsonify(genres_schema.dump(all_genres))

    def post(self):
        req_json = request.json
        new_genre = Genre(**req_json)
        with db.session.begin():
            db.session.add(new_genre)
        return "", 201


@genres_ns.route('/<int:uid>')
class GenreView(Resource):
    def get(self, uid):
        genre = Genre.query.get(uid)
        return jsonify(genre_schema.dump(genre))

    def put(self, uid: int):
        genre = Genre.query.get(uid)
        req_json = request.json
        set_keys(req_json, genre)
        db.session.add(genre)
        db.session.commit()
        return "", 204

    def delete(self, uid: int):
        genre = Genre.query.get(uid)
        db.session.delete(genre)
        db.session.commit()
