from flask import Flask
from flask_restx import Api, Resource, fields
from environments import config
import logging
from resources.boardgames import api as boardgames_api_namespace

app = Flask(__name__)
api = Api(app,
          version='0.3',
          title="Boardgame API",
          description="a description"
)

api.add_namespace(boardgames_api_namespace)

# @api.route('/my-resource/<id>')
# @api.doc(params={'id': 'An ID'})
# class MyResource(Resource):
#     def get(self, id):
#         return {"id": id}

#     @api.response(403, 'Not Authorized')
#     def post(self, id):
#         api.abort(403)

if __name__ == '__main__':
    logging.basicConfig(filename=config.log_path, level=logging.DEBUG)
    logging.info("Start boardgame collection service...")
    print("Started on http://localhost:{0}".format(config.port))
    app.run(debug=config.debug, port=config.port)