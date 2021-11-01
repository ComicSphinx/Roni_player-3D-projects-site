# @Author: Daniil Maslov (ComicSphinx)

from flask import Flask, jsonify, request
from flask.wrappers import Response
from flask_restful import Api, Resource

from Database import Database

app = Flask(__name__)
api = Api(app)

class PresentationService(Resource):

    localhost = "127.0.0.1:5000/"

    @app.route('/presentation/<id>', methods=['GET'])
    def getPresentationById(id):
        # textData = {'title': 'Title dmmaslov', 'presentationTitle': 'Title', 'description': 'Description'}
        # response = jsonify(textData)
        # response.status_code = 200
        # response.headers['Access-Control-Allow-Origin'] = '*'

        presentation = Database.getPresentationById(Database, id)
        if presentation == []:
            return("record not found") # тут надо возвращать еще какой-то код, типа 400
        else: 
            return jsonify(presentation)

api.add_resource(PresentationService, "/")
if __name__ == "__main__":
    app.run(debug=True)
    Database.secureInitDB(Database)
    