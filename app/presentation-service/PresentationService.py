# @Author: Daniil Maslov (ComicSphinx)

from flask import Flask, url_for, redirect
from flask.templating import render_template
from flask_restful import Api, Resource
import requests
from requests.exceptions import JSONDecodeError

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

DB_SERVICE_BASE_URL = 'http://127.0.0.1'

class PresentationService(Resource):

    @app.route('/presentation/<id>', methods=['GET'])
    def presentation(id):
        # Отправить запрос, получить ответ
        url = DB_SERVICE_BASE_URL+'/presentation/'+id
        data = requests.get(url)
        try:
            data = data.json()
            return render_template('presentation.html', data=data)
        except JSONDecodeError:
            return redirect(url_for('presentationsList'))

    @app.route('/presentationsList/', methods=['GET'])
    def presentationsList():
        # Отправить запрос, получить ответ
        url = DB_SERVICE_BASE_URL+'/getPresentationsListData'
        data = requests.get(url).json()

        return render_template('presentationsList.html', presentationsList=data)

api.add_resource(PresentationService)
if __name__ == "__main__":
    app.run(port=81, debug=True)