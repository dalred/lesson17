from flask_restx import Resource, Namespace
from flask import request, jsonify
from app.schemas import *
from app.models import *
from app.functions import set_keys

movies_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)

@movies_ns.route('/')
class MoviesView(Resource):
    def get(self):
        director_id = request.args.get('director_id')
        genre_id = request.args.get('genre_id')
        all_movies = db.session.query(Movie)
        if director_id:
            all_movies = all_movies.filter(Director.id == director_id).join(
                Director)
        if genre_id:
            all_movies = all_movies.filter(Genre.id == genre_id).join(Genre)
        all_movies = all_movies.all()
        return jsonify(movies_schema.dump(all_movies))

@movies_ns.route('/<int:uid>')
class MovieView(Resource):
    def get(self, uid):
        movie = Movie.query.get(uid)
        return jsonify(movie_schema.dump(movie))
