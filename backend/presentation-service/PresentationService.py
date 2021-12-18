# @Author: Daniil Maslov (ComicSphinx)

from flask import Flask
from flask.templating import render_template
from flask_restful import Api, Resource # TODO: Верно ли я применяю flask_restful?

from Database import Database

app = Flask(__name__)
api = Api(app)

class PresentationService(Resource):

    @app.route('/presentation/<id>', methods=['GET'])
    def presentation(id):
        # TODO:
        # 1. Подтянуть картинки из базы по id
        # 2. Подтянуть текстовые данные из базы по id
        # 3. Отрендерить картинку с полученными из базы данными, отдавая в html словарь
        output = {} # TODO: Зарефакторить название переменной
        
        # TODO: Зарфеакторить фрагмент
        pageTitle = Database.getPresentationById(Database, id, 'title')
        descriptionTitle = Database.getPresentationById(Database, id, 'descriptionTitle')
        description = Database.getPresentationById(Database, id, 'description')
        firstImage = Database.getPresentationById(Database, id, 'firstImage')
        secondImage = Database.getPresentationById(Database, id, 'secondImage')
        thirdImage = Database.getPresentationById(Database, id, 'thirdImage')
        fourthImage = Database.getPresentationById(Database, id, 'fourthImage')
        fifthImage = Database.getPresentationById(Database, id, 'fifthImage')
        sixthImage = Database.getPresentationById(Database, id, 'sixthImage')
        seventhImage = Database.getPresentationById(Database, id, 'seventhImage')
        eightImage = Database.getPresentationById(Database, id, 'eightImage')
        mainImage = Database.getPresentationById(Database, id, 'mainImage')

        output = {'pageTitle':pageTitle, 'descriptionTitle': descriptionTitle, 'description': description, 'firstImage': firstImage, 'secondImage': secondImage,
                    'thirdImage': thirdImage, 'fourthImage': fourthImage, 'fifthImage': fifthImage, 'sixthImage': sixthImage, 'seventhImage': seventhImage, 'eightImage': eightImage,
                    'mainImage': mainImage}
        
        return render_template('presentation.html', data=output)

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
    Database.secureInitDB(Database)