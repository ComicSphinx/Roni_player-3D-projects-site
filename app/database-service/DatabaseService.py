# @Author: Daniil Maslov (ComicSphinx)

from flask_restful import Api, Resource
from Models import Presentation, app

api = Api(app)

class DatabaseService(Resource):

    @app.route('/getPresentationDataById/<id>', methods=['GET'])
    def getPresentationById(id):
        presentation = Presentation.query.filter_by(id=id).first_or_404()
        
        return Presentation.serialize(presentation)

api.add_resource(DatabaseService)
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=80, debug=True)