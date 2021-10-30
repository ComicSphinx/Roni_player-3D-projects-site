# @Author: Daniil Maslov (ComicSphinx)

from flask import Flask, jsonify, request
from flask.wrappers import Response
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class presentation(Resource):

    @app.route("/presentation", methods=['GET'])
    def get():
        textData = {'title': 'Title dmmaslov', 'presentationTitle': 'Title', 'description': 'Description'}
        response = jsonify(textData)
        response.status_code = 200
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response

api.add_resource(presentation, "/")
if __name__ == "__main__":
    app.run(debug=True)