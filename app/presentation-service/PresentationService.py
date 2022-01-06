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
        # TODO: ЗАРЕФАКТОРИТЬ
        url = 'http://127.0.0.1/getPresentationById/'+id
        data = requests.get(url).json()
        
        return render_template('presentation.html', data=data)

    @app.route('/presentationsList/', methods=['GET'])
    def presentationsList():
        # TODO: Можно использовать структуру - словарь, ids - первое значение, PresentationsImagesPath - второе
        ids = []
        ids1 = [] #TODO : ЗАРЕФАКТОРИТЬ И НЕ ЗАБЫТЬ ПОМЕНЯТЬ В HTML
        presentationsImagesPaths = []
        presentationsImagesPaths1 = [] #TODO : ЗАРЕФАКТОРИТЬ И НЕ ЗАБЫТЬ ПОМЕНЯТЬ В HTML
        output = {} # TODO: Зарефакторить название переменной

        # Заполняем ids и presentationsImagesPaths
        ids = Database.getPresentationsList(Database, 'presentationId')
        presentationsImagesPaths = Database.getPresentationsList(Database, 'mainImage')

        # Уменьшаем вложенность
        i = 0
        for i in range(len(ids)):
            ids1.append(ids[i][0])
            presentationsImagesPaths1.append(presentationsImagesPaths[i][0])

        # добавляем ids и presentationsImagesPath в outputDict
        i = 0
        for i in range(len(ids1)):
            output.update({ids1[i]: presentationsImagesPaths1[i]})

        # Отобразить страинчку со списком презентаций, в качестве аргумента отдаем картинки и id TODO: что отдавать вторым аргументом, чтобы в html я смог построить ссылочки на карточки?
        return render_template('presentationsList.html', presentationsList=output)

api.add_resource(PresentationService)
if __name__ == "__main__":
    app.run(debug=True)