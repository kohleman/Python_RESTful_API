from flask_restx import fields

def create_expansion_model(api):
    expansion_model = api.model('Expansion', {
      'name': fields.String(description='boardgame expansion name',
                            min_length=3,
                            max_length=128,
                            required=True),
      'rating': fields.Float(description='rating [0 to 10]',
                             min=0.0,
                             max=10.0,
                             required=False)
    })
    return expansion_model