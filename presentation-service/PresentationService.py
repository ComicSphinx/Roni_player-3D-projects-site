# @Author: Daniil Maslov (ComicSphinx)

from flask import Flask, jsonify
from flask.templating import render_template
from flask_restful import Api, Resource
from flask_migrate import Migrate
from flask_sslify import SSLify
import sys
sys.path.append('database/')
from Models import Presentation, app, db

app = Flask(__name__)
migrate = Migrate(app, db)
api = Api(app)
sslify = SSLify(app)
db.init_app(app)

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
    app.run(debug=True)