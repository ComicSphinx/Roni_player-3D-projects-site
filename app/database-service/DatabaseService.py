# @Author: Daniil Maslov (ComicSphinx)

from flask_restful import Api, Resource
from Models import Presentation, app
from flask import jsonify

api = Api(app)

class DatabaseService(Resource):

    @app.route('/getPresentationDataById/<id>', methods=['GET'])
    def getPresentationById(id):
        presentation = Presentation.query.filter_by(id=id).first_or_404()
        
        return Presentation.serialize(presentation)

    @app.route('/getPresentationsListData', methods=['GET'])
    def getPresentationsListData():
        presentationsList = Presentation.query.filter_by(active='True').all()
        result = []
        
        for i in presentationsList:
            result.append(Presentation.serialize(i))
        
        return jsonify(result)

api.add_resource(DatabaseService)
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=80, debug=True)