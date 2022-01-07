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
        # TODO: ссылку надо вынести в константу
        url = 'http://127.0.0.1/getPresentationsListData'
        data = requests.get(url).json()

        return render_template('presentationsList.html', presentationsList=data)

api.add_resource(PresentationService)
if __name__ == "__main__":
    app.run(debug=True)