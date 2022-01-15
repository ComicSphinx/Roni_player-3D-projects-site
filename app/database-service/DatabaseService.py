# @Author: Daniil Maslov (ComicSphinx)

from flask_restful import Api, Resource
from werkzeug.utils import secure_filename, send_file
from Models import Presentation, app, db
from flask import jsonify, request, send_file
import os

api = Api(app)
app.secret_key = "b'z\x8a#\n8\x06\xe2\xd5\xe7\xba\x0c\xbc\xc6\x1d&*'"

UPLOAD_FOLDER_PATH = 'static/presentations/'
NOT_SUPPORTED_REQUEST_TYPE_ERROR_MESSAGE = 'Can not handle this request'

class DatabaseService(Resource):

    @app.route('/presentation/<id>', methods=['GET'])
    def getPresentation(id):
        if request.method == 'GET':
            presentation = Presentation.query.filter_by(id=id).first_or_404()
            return Presentation.serialize(presentation)
        else:
            return NOT_SUPPORTED_REQUEST_TYPE_ERROR_MESSAGE, 400

    @app.route('/getPresentationsListData', methods=['GET'])
    def getPresentationsListData():
        if request.method == 'GET':
            presentationsList = Presentation.query.filter_by(active=True).all()
            result = []

            for i in presentationsList:
                result.append(Presentation.serialize(i))

            return jsonify(result)
        else:
            return NOT_SUPPORTED_REQUEST_TYPE_ERROR_MESSAGE, 400

    @app.route('/getPresentation/<id>/image/<imageFieldName>', methods=['GET'])
    def getImageByPresentationIdAndFieldName(imageFieldName, id):
        if request.method == 'GET':
            presentation = DatabaseService.getPresentation(id)
            filename = presentation.get(imageFieldName)
            path = UPLOAD_FOLDER_PATH+str(id)+'/'+filename
            return send_file(path, mimetype='image/jpeg')
        else:
            return NOT_SUPPORTED_REQUEST_TYPE_ERROR_MESSAGE, 400

    @app.route('/deletePresentations', methods=['POST'])
    def deletePresentations():
        if request.method == 'POST':
            print(request.form.getlist('id'))
            return "successful"
        else:
            return NOT_SUPPORTED_REQUEST_TYPE_ERROR_MESSAGE, 400

    # TODO: переименовать в createPresentation
    @app.route('/presentation', methods=['POST'])
    def createPresentation():
        if request.method == 'POST':
            # Get title, description and images from request
            title = request.form.get('title')
            description = request.form.get('description')
            images = DatabaseService.getImagesFromRequest()

            # Generate ID for a new presentation
            newPresentationId = DatabaseService.getNewPresentationId()

            # Create Presentation Object and it to database
            newPresentation = Presentation(newPresentationId, title, description,
                                            secure_filename(images[0].filename), secure_filename(images[1].filename),
                                            secure_filename(images[2].filename), secure_filename(images[3].filename),
                                            secure_filename(images[4].filename), secure_filename(images[5].filename),
                                            secure_filename(images[6].filename), secure_filename(images[7].filename),
                                            secure_filename(images[0].filename), True)
            DatabaseService.savePresentationToDb(newPresentation)

            # Create new dir and save there images
            DatabaseService.createPresentationDir(newPresentationId)
            DatabaseService.savePresentationImagesToDir(images, newPresentationId)

            return "successful"

    def getImagesFromRequest():
        images = []
        filename = 'file'
        for number in range(8):
            fullFilename = filename+str(number)
            images.append(request.files[fullFilename])
        
        return images

    def createPresentationDir(id):
        path = UPLOAD_FOLDER_PATH+str(id)
        os.mkdir(path)

    def getMaxId():
        presentationsList = Presentation.query.all()
        maxId = 0
        for i in presentationsList:
            if i.id > maxId:
                maxId = i.id
        return maxId

    def getNewPresentationId():
        return DatabaseService.getMaxId()+1

    # Сохранить картинки
    def savePresentationImagesToDir(images, dirId):
        for i in range(len(images)):
            filename = secure_filename(images[i].filename)
            path = UPLOAD_FOLDER_PATH+str(dirId)+'/'+filename
            images[i].save(path)

    # На вход принимает класс с заполненными полями
    def savePresentationToDb(newPresentation):
        db.session.add(newPresentation)
        db.session.commit()

api.add_resource(DatabaseService)
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=80, debug=True)