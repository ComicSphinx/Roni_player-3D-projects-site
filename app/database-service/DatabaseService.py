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
    def savePresentation():
        file0 = request.files['file0']
        file1 = request.files['file1']
        file2 = request.files['file2']
        file3 = request.files['file3']
        file4 = request.files['file4']
        file5 = request.files['file5']
        file6 = request.files['file6']
        file7 = request.files['file7']
        

        # TODO: папку надо создавать после того, как убедимся, что были получены все 8 файлов
        dirId = DatabaseService.getMaxId()+1
        DatabaseService.createPresentationDir(dirId)

        DatabaseService.saveImages(file0, file1, file2, file3, file4, file5, file6, file7, dirId)
            
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
    def saveImages(file0, file1, file2, file3, file4, file5, file6, file7, dirId):
        filename = secure_filename(file0.filename)
        path = UPLOAD_FOLDER_PATH+str(dirId)+'/'+filename
        file0.save(path)
        filename = secure_filename(file1.filename)
        path = UPLOAD_FOLDER_PATH+str(dirId)+'/'+filename
        file1.save(path)
        filename = secure_filename(file2.filename)
        path = UPLOAD_FOLDER_PATH+str(dirId)+'/'+filename
        file2.save(path)
        filename = secure_filename(file3.filename)
        path = UPLOAD_FOLDER_PATH+str(dirId)+'/'+filename
        file3.save(path)
        filename = secure_filename(file4.filename)
        path = UPLOAD_FOLDER_PATH+str(dirId)+'/'+filename
        file4.save(path)
        filename = secure_filename(file5.filename)
        path = UPLOAD_FOLDER_PATH+str(dirId)+'/'+filename
        file5.save(path)
        filename = secure_filename(file6.filename)
        path = UPLOAD_FOLDER_PATH+str(dirId)+'/'+filename
        file6.save(path)
        filename = secure_filename(file7.filename)
        path = UPLOAD_FOLDER_PATH+str(dirId)+'/'+filename
        file7.save(path)

    # Сохранить данные в таблицу
    def saveData():
        print()

api.add_resource(DatabaseService)
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=80, debug=True)
    DatabaseService.getMaxId()