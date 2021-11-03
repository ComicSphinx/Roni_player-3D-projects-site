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
        fields = ['presentation_id', 'title', 'description', 'description_title', 'first_img', 'second_img', 
                    'third_img', 'fourth_img', 'fifth_img', 'sixth_img', 'seventh_img', 'eight_img', 'active']
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
                presentation_id=presentationData[0],
                title=presentationData[1],
                description=presentationData[2],
                presentationTitle=presentationData[3],
                firstImg=presentationData[4],
                secondImg=presentationData[5],
                thirdImg=presentationData[6],
                fourthImg=presentationData[7],
                sixthImg=presentationData[8],
                seventhImg=presentationData[9],
                eightImg=presentationData[10],
                active=presentationData[11]
            )
            # TODO: До введения в пром.эксплуатацию надо, скорее всего, убрать этот хедер и настроить безопасность
            
            return make_response(json, {'Access-Control-Allow-Origin': '*'})

    @app.route('/presentationImages/<id>', methods=['GET'])
    def getPresentationImagesById(id):
        image_path = 'db/images/1.jpg'
        
        # TODO: До введения в пром.эксплуатацию надо, скорее всего, убрать этот хедер и настроить безопасность
        return make_response(send_file(image_path, mimetype='image/gif'), {'Access-Control-Allow-Origin': '*'})
        

api.add_resource(PresentationService, "/")
if __name__ == "__main__":
    app.run(debug=True)
    Database.secureInitDB(Database)