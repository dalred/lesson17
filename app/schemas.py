from marshmallow import Schema, fields

class DirectorSchema(Schema):
    __tablename__ = 'director'
    id = fields.Int(dump_only=True)
    name = fields.Str()


class GenreSchema(Schema):
    __tablename__ = 'genre'
    id = fields.Int(dump_only=True)
    name = fields.Str()


class MovieSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Float()
    director = fields.Pluck('DirectorSchema', "name", many=False)
    genre = fields.Pluck('GenreSchema', "name", many=False)