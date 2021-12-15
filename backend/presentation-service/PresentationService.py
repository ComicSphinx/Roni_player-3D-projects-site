# @Author: Daniil Maslov (ComicSphinx)

from flask import Flask, jsonify, make_response, send_file
from flask.templating import render_template
from flask_restful import Api, Resource

from Database import Database

app = Flask(__name__)
api = Api(app)

class PresentationService(Resource):

    @app.route('/presentationText/<id>', methods=['GET'])
    def getPresentationTextById(id):
        fields = ['presentationId', 'title', 'description', 'descriptionTitle', 'active']
        presentationDataDraft = []
        presentationData = []

        # получаем данные, заполнить presentationDataDraft
        i=0
        for i in range(len(fields)):
            presentationDataDraft.append(Database.getPresentationById(Database, id, fields[i]))

        # Уменьшаем вложенность данных (иначе будет, примерно, так - ([[1]], [[2]]))
        i=0
        for i in range(len(presentationDataDraft)):
            presentationData.append(presentationDataDraft[i][0][0])
        
        if presentationData[0] == '':
             # TODO: тут надо возвращать еще какой-то код и ответ, типа 400
            return("record not found")
        else:
            # TODO: полагаю, это надо будет зарефакторить
            json = jsonify(
                presentationId=presentationData[0],
                title=presentationData[1],
                description=presentationData[2],
                presentationTitle=presentationData[3],
                active=presentationData[4]
            )

            # TODO: До введения в пром.эксплуатацию надо, скорее всего, убрать этот хедер и настроить безопасность
            return make_response(json, {'Access-Control-Allow-Origin': '*'})

    @app.route('/presentationImage/<id>/<strImageNumber>', methods=['GET'])
    def getPresentationImagesById(id, strImageNumber):
        imagePath = Database.getPresentationById(Database, id, strImageNumber)
        
        # TODO: До введения в пром.эксплуатацию надо, скорее всего, убрать этот хедер и настроить безопасность
        return make_response(send_file(imagePath[0][0], mimetype='image/jpeg'), {'Access-Control-Allow-Origin': '*'})
    
    # # TODO: Сделать рефакторинг. У меня два, почти одинаковых, метода
    # @app.route('/presentationsList', methods=['GET'])
    # def getPresentationsList():
    #     fields = ['presentationId', 'count(presentationId)']
    #     presentationDataDraft = []
    #     ids = []

    #     # Получаем список id
    #     presentationDataDraft.append(Database.getPresentationsList(Database, fields[0]))
    #     print(presentationDataDraft[0])
    #     # TODO: Заполняем поле count (count вызывает этот метод - беспорядок, т.к. метод должен возвращать СПИСОК)
    #     count = Database.getPresentationsList(Database, fields[1])
    
    #     # Уменьшаем вложенность данных для ids (иначе будет, примерно, так - ([[1]], [[2]]))
    #     i=0
    #     for i in range(len(presentationDataDraft[0])):
    #         ids.append(presentationDataDraft[0][i][0])

    #     # Уменьшаем вложенность данных для count
    #     count = count[0][0]
        
    #     # TODO: говно, а не обработчик
    #     if ids[0] == '':
    #          # TODO: тут надо возвращать еще какой-то код и ответ, типа 400
    #         return("record not found")
    #     else:
    #         # TODO: полагаю, это надо будет зарефакторить
    #         json = jsonify(
    #             presentationIds=ids,
    #             count=count
    #         )

    @app.route('/presentationsList', methods=['GET'])
    def getPresentationsList():
        # TODO: Можно использовать структуру - словарь, ids - первое значение, PresentationsImagesPath - второе
        ids = []
        ids1 = [] #TODO : ЗАРЕФАКТОРИТЬ
        presentationsImagesPaths = []
        presentationsImagesPaths1 = [] #TODO : ЗАРЕФАКТОРИТЬ
        outputDict = {}

        # Заполняем ids и presentationsImagesPaths
        ids = Database.getPresentationsList(Database, 'presentationId')
        presentationsImagesPaths = Database.getPresentationsList(Database, 'firstImage')

        # Уменьшаем вложенность
        i = 0
        for i in range(len(ids)):
            ids1.append(ids[i][0])
            presentationsImagesPaths1.append(presentationsImagesPaths[i][0])

        # добавляем ids и presentationsImagesPath в outputDict
        i = 0
        for i in range(len(ids1)):
            outputDict.update({ids1[i]: presentationsImagesPaths1[i]})

        # Отобразить страинчку со списком презентаций, в качестве аргумента отдаем картинки и id TODO: что отдавать вторым аргументом, чтобы в html я смог построить ссылочки на карточки?
        return render_template('presentationsList.html')

api.add_resource(PresentationService, "/")
if __name__ == "__main__":
    app.run(debug=True)
    Database.secureInitDB(Database)