# @Author: Daniil Maslov (ComicSphinx)

from flask import Flask
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from Presentation import Presentation

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

class DatabaseService(Resource):

    @app.route('/getPresentationById/<id>', methods=['GET'])
    def getPresentationById(id):
        presentation = Presentation()
        data = presentation.query.filter_by(presentationId=id).first()

        return data.title
    

api.add_resource(DatabaseService)
if __name__ == "__main__":
    db = SQLAlchemy()
    db.init_app(app)
    app.run(host='127.0.0.1', port=80, debug=True)
