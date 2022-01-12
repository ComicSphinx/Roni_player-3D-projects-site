# @Author: Daniil Maslov (ComicSphinx)

from flask_restful import Api, Resource
from werkzeug.utils import secure_filename, send_file
from Models import Presentation, app, db
from flask import jsonify, request, send_file
import os

api = Api(app)
app.secret_key = "b'z\x8a#\n8\x06\xe2\xd5\xe7\xba\x0c\xbc\xc6\x1d&*'"

UPLOAD_FOLDER_PATH = 'static/presentations/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'} # TODO: ПРИМЕНИТЬ

class DatabaseService(Resource):

    @app.route('/getPresentationDataById/<id>', methods=['GET'])
    def getPresentationDataById(id):
        presentation = Presentation.query.filter_by(id=id).first_or_404()
        
        return Presentation.serialize(presentation)

    @app.route('/getPresentationsListData', methods=['GET'])
    def getPresentationsListData():
        presentationsList = Presentation.query.filter_by(active=True).all()
        result = []
        
        for i in presentationsList:
            result.append(Presentation.serialize(i))
        
        return jsonify(result)

    # TODO: зарефаткорить, метод не должен так называться, и взаимодействие так себе, и название полей
    @app.route('/getImage/<imageName>/ByPresentationId/<presentationId>')
    def getImageByPresentationId(imageName, presentationId):
        presentation = DatabaseService.getPresentationDataById(presentationId)
        filename = presentation.get(imageName)
        path = UPLOAD_FOLDER_PATH+str(presentationId)+'/'+filename
        return send_file(path, mimetype='image/jpeg')

    # TODO: Рефакторинг
    # TODO: Функция не должна делать так много, большую часть следует вынести в маленькие функции
    @app.route('/Presentation', methods=['POST'])
    def Presentation():
        # get title and description
        title = request.form.get('title')
        description = request.form.get('description')
        images = DatabaseService.getImagesFromRequest()

        # TODO: папку надо создавать после того, как убедимся, что были получены все 8 файлов
        newPresentationId = DatabaseService.getMaxId()+1
        DatabaseService.createPresentationDir(newPresentationId)

        DatabaseService.saveImages(images, newPresentationId)
    
        # TODO: тут надо будет писать True вместо 'True', когда разберусь с булевностью поля
        newPresentation = Presentation(newPresentationId, title, description,
                                        secure_filename(images[0].filename), secure_filename(images[1].filename),
                                        secure_filename(images[2].filename), secure_filename(images[3].filename),
                                        secure_filename(images[4].filename), secure_filename(images[5].filename),
                                        secure_filename(images[6].filename), secure_filename(images[7].filename),
                                        secure_filename(images[0].filename), True) # последнее - это main
        DatabaseService.saveData(newPresentation)

        return "successful"

    def getImagesFromRequest():
        images = []
        filename = 'file'
        for number in range(8):
            fullFilename = filename+str(number)
            images.append(request.files[fullFilename])
        
        return images

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
    def saveImages(images, dirId):
        for i in range(len(images)):
            filename = secure_filename(images[i].filename)
            path = UPLOAD_FOLDER_PATH+str(dirId)+'/'+filename
            images[i].save(path)

    # Сохранить данные в таблицу
    # На вход принимает класс с заполненными полями
    def saveData(newPresentation):
        db.session.add(newPresentation)
        db.session.commit()

api.add_resource(DatabaseService)
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=80, debug=True)