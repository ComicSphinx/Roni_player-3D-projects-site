# @Author: Daniil Maslov (ComicSphinx)

from flask_restful import Api, Resource
from werkzeug.utils import secure_filename
from Models import Presentation, app
from flask import jsonify, request, flash
import os

api = Api(app)
app.secret_key = "b'z\x8a#\n8\x06\xe2\xd5\xe7\xba\x0c\xbc\xc6\x1d&*'"

UPLOAD_FOLDER_PATH = 'static/presentations/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER_PATH'] = UPLOAD_FOLDER_PATH

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

    # TODO: Рефакторинг
    # TODO: Осталось решить проблему - оно сохраняет только один файл
    @app.route('/savePresentation', methods=['POST'])
    def addPresentation():
        nextId = DatabaseService.getMaxId()+1
        DatabaseService.createPresentationDir(nextId)

        if 'file' not in request.files:
            flash('no selected files')
        uploadedFiles = request.files['file']
        
        if uploadedFiles.filename == '':
            flash('no selected files')
        
        # сделать обработку на корректный тип файла (https://flask.palletsprojects.com/en/1.1.x/patterns/fileuploads/)
        if uploadedFiles:
            filename = secure_filename(uploadedFiles.filename)
            path = UPLOAD_FOLDER_PATH+str(nextId)+'/'+filename
            uploadedFiles.save(path)
        # DatabaseService.saveImages(uploadedFiles, nextId)
        return "successful"

    def createPresentationDir(id):
        # TODO: Надо сделать обработку ошибок, когда не получилось создать папку
        path = UPLOAD_FOLDER_PATH+str(id)
        os.mkdir(path)

    def getMaxId():
        presentationsList = Presentation.query.all()
        maxId = 0
        for i in presentationsList:
            if i.id > maxId:
                maxId = i.id
        return maxId    

    # Сохранить картинки
    def saveImages(files, dirId):
        for file in files:
            filename = secure_filename(file.filename)
            path = UPLOAD_FOLDER_PATH+str(dirId)
            file.save(os.path.join(path), filename)

    # Сохранить данные в таблицу
    def saveData():
        print()

api.add_resource(DatabaseService)
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=80, debug=True)
    DatabaseService.getMaxId()