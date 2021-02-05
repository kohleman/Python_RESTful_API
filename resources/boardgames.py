from flask_restx import Namespace, Resource
from flask import abort, request
from http import HTTPStatus

bg_collection = {} # boardgames stored in memory
api = Namespace('boardgames', description='boardgame related operations')

@api.route('/<id>')
class Boardgame(Resource):
    def get(self, id):
      '''Gets a boardgame by id'''
      if id in bg_collection:
        return bg_collection[id], HTTPStatus.OK
      else:
          abort(HTTPStatus.NOT_FOUND, 'Boardgame {0} not found.' .format(id))

    def delete(self, id):
      '''Removes a boardgame from the collection'''
      if id in bg_collection:
        del bg_collection[id]
        return '', HTTPStatus.NO_CONTENT
      else:
        abort(HTTPStatus.NOT_FOUND, 'Boardgame {0} not found.' .format(id))

    def put(self, id):
      '''Updates a boardgame'''
      boardgame = request.get_json
      if id in bg_collection:
        bg_collection[id] = boardgame
        return boardgame, HTTPStatus.OK
      else:
        abort(HTTPStatus.NOT_FOUND, 'Boardgame {0} not found.' .format(id))

@api.route('')
class BoardgameList(Resource):
    def get(self):
      '''Lists all boardgames in collection'''
      bg_collection_list = list(bg_collection.values())
      return bg_collection_list, HTTPStatus.OK

    @api.response(201, 'Boardgame successfully created')
    def post(self):
      '''Adds a boardgame to collection'''
      boardgame = request.json
      print(request.is_json)
      print(boardgame)
      bg_collection[boardgame['id']] = boardgame
      return boardgame, HTTPStatus.CREATED