from flask_restx import Namespace, Resource
from flask import abort, request
from http import HTTPStatus
from models.boardgame_model import create_boardgame_model

bg_collection = {}  # boardgames stored in memory
api = Namespace('boardgames', description='boardgame related operations')

boardgame = create_boardgame_model(api)


@api.param('id', 'The boardgame identifier.')
@api.response(404, 'Boardgame not found.')
@api.route('/<id>')
class Boardgame(Resource):
    @api.marshal_with(boardgame)
    def get(self, id):
        '''Gets a boardgame by id'''
        if id in bg_collection:
            return bg_collection[id], HTTPStatus.OK
        else:
            abort(HTTPStatus.NOT_FOUND, 'Boardgame {0} not found.' .format(id))

    @api.response(204, 'Boardgame successfully deleted.')
    def delete(self, id):
        '''Removes a boardgame from the collection'''
        if id in bg_collection:
            del bg_collection[id]
            return '', HTTPStatus.NO_CONTENT
        else:
            abort(HTTPStatus.NOT_FOUND, 'Boardgame {0} not found.' .format(id))

    @api.response(200, 'Boardgame successfully updated.')
    @api.expect(boardgame, validate=True)
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

    @api.param('offset',
               'The offset of the first boardgame in the list to return.',
               type=int,
               default=0)
    @api.param('limit',
               'The maximum number of boardgames to return.',
               type=int,
               default=100)
    @api.param('sort_by',
               'Sort the returned boardgames by key.',
               default="id",
                enum=["id", "name", "designer", "rating"])
    @api.param('sort_order',
               'Ascending or descending sort order.',
               default="asc", enum=["asc", "desc"])
    @api.marshal_list_with(boardgame)
    @api.response(200, 'All boardgames successfully fetched!')
    def get(self):
        '''Lists all boardgames in collection'''
        # the parameters for offset,  limit, sorting and order can be passed on here:
        offset = request.args.get('offset')
        print(offset)
        bg_collection_list = list(bg_collection.values())
        return bg_collection_list, HTTPStatus.OK

    @api.expect(boardgame, validate=True)
    @api.response(201, 'Boardgame successfully created')
    def post(self):
        '''Adds a boardgame to collection'''
        boardgame = request.json
        print(request.is_json)
        print(boardgame)
        bg_collection[boardgame['id']] = boardgame
        return boardgame, HTTPStatus.CREATED