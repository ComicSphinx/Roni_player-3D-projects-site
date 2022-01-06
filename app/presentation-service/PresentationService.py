# @Author: Daniil Maslov (ComicSphinx)

from flask import Flask, request
from flask.templating import render_template
from flask_restful import Api, Resource
import requests

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
class PresentationService(Resource):

    @app.route('/presentation/<id>', methods=['GET'])
    def presentation(id):
        # TODO: Ссылку мб надо вынести в константу. Либо хранить в отдельном файле.
        url = 'http://127.0.0.1/getPresentationDataById/'+id
        data = requests.get(url).json()

        return render_template('presentation.html', data=data)

    @app.route('/presentationsList/', methods=['GET'])
    def presentationsList():
        # Запросить список в дб, отобразить

        return render_template('presentationsList.html', presentationsList=output)

api.add_resource(PresentationService)
if __name__ == "__main__":
    app.run(debug=True)