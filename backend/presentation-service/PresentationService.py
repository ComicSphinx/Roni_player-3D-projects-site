# @Author: Daniil Maslov (ComicSphinx)

from flask import Flask, jsonify, request
from flask.wrappers import Response
from flask_restful import Api, Resource

from Database import Database

app = Flask(__name__)
api = Api(app)

class PresentationService(Resource):

    localhost = "127.0.0.1:5000/"

    @app.route('/presentation/<id>', methods=['GET'])
    def getPresentationById(id):
        fields = ['presentation_id', 'title', 'description', 'description_title', 'first_img', 'second_img', 
                    'third_img', 'fourth_img', 'fifth_img', 'sixth_img', 'seventh_img', 'eight_img', 'active']
        presentationData = []
        response = []

        # получаем данные, заполнить presentationData
        i=0
        for i in range(len(fields)):
            presentationData.append(Database.getPresentationById(Database, id, fields[i]))

        # Уменьшаем вложенность данных (иначе будет, примерно, так - ([[1]], [[2]]))
        i=0
        for i in range(len(presentationData)):
            response.append(presentationData[i][0][0])
        
        if presentationData[0] == '':
             # TODO: тут надо возвращать еще какой-то код и ответ, типа 400
            return("record not found")
        else:
            # TODO: полагаю, это надо будет зарефакторить
            return jsonify(
                presentation_id=response[0],
                title=response[1],
                description=response[2],
                descriptionTitle=response[3],
                firstImg=response[4],
                secondImg=response[5],
                thirdImg=response[6],
                fourthImg=response[7],
                sixthImg=response[8],
                seventhImg=response[9],
                eightImg=response[10],
                active=response[11]
            )

api.add_resource(PresentationService, "/")
if __name__ == "__main__":
    app.run(debug=True)
    Database.secureInitDB(Database)