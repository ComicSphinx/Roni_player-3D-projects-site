# @Author: Daniil Maslov (ComicSphinx)

from flask import Flask, url_for, redirect, jsonify
from flask.templating import render_template
from flask_restful import Api, Resource
import requests
from requests.exceptions import JSONDecodeError

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://gdjqbznobxhqxk:cf39ce62f344cfa9cb15eba8c31a6e0304f42750e5f69a3563da7505f1f80fb5@ec2-3-212-143-188.compute-1.amazonaws.com:5432/d5hggk2n1g9v3n'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# TODO: СКОРРЕКТИРОВАТЬ НАИМЕНОВАНИЕ И ПУТЬ
UPLOAD_FOLDER_PATH = 'static/presentations/'

class PresentationService(Resource):

    @app.route('/presentation/<id>', methods=['GET'])
    def presentation(id):
        # Получить презентацию
        presentation = PresentationService.getPresentationById(id)
        
        # Возможно, надо будет делать .json
        return render_template('presentation.html', data=presentation)

    @app.route('/presentationsList/', methods=['GET'])
    def presentationsList():
        # Получить список презентаций
        presentationList = PresentationService.getPresentationsList()

        # мб надо будет делать .json
        return render_template('presentationsList.html', presentationsList=presentationList)

    def getPresentationById(id):
        presentation = Presentation.query.filter_by(id=id, active=True).first_or_404()
        return Presentation.serialize(presentation)

    def getPresentationsList():
        presentationsList = Presentation.query.filter_by(active=True).all()
        presentationsListSerialized = []

        for i in presentationsList:
            presentationsListSerialized.append(Presentation.serialize(i))

        return jsonify(presentationsListSerialized)

api.add_resource(PresentationService)
if __name__ == "__main__":
    app.run(port=81, debug=True)