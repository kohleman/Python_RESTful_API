from flask_restx import fields
from models.expansion_model import create_expansion_model

def create_boardgame_model(api):
    boardgame_model = api.model('Boardgame', {
      'id': fields.String(description='unique boardgame identifier',
                          required=True),
      'name': fields.String(description='boardgame name',
                            min_length=3,
                            max_length=128,
                            required=True),
      'designer': fields.String(description='boardgame designer',
                                required=True),
      'playing_time': fields.String(description='aprox. playing time',
                                    enum=["15 Min", "30 Min", "60 Min"],
                                    required=True),
      'rating': fields.Float(description='rating [0 to 10]',
                             min=0.0,
                             max=10.0,
                             required=False),
      'expansions': fields.List(fields.Nested(create_expansion_model(api),
                                              description='list of expansions',
                                              required=False))
    })

    return boardgame_model