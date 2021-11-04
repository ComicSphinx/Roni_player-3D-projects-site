# @Author: Daniil Maslov (ComicSphinx)

from flask import Flask, jsonify, make_response, send_file
from flask.templating import render_template
from flask_restful import Api, Resource

from Database import Database

app = Flask(__name__)
api = Api(app)

class PresentationService(Resource):

    localhost = "127.0.0.1:5000/"

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
        print(type(imagePath))
        print(imagePath)
        return make_response(send_file(imagePath[0][0], mimetype='image/jpeg'), {'Access-Control-Allow-Origin': '*'})
        

api.add_resource(PresentationService, "/")
if __name__ == "__main__":
    app.run(debug=True)
    Database.secureInitDB(Database)