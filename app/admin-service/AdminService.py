# @Author: Daniil Maslov (ComicSphinx)

from flask import Flask, session, redirect, url_for, request, jsonify
from flask.templating import render_template
from werkzeug.utils import secure_filename
from flask_restful import Api, Resource
from flask_migrate import Migrate
from flask_sslify import SSLify
import os
import sys
sys.path.append('../database')
from Models import Presentation, app, db

app = Flask(__name__)
migrate = Migrate(app, db)
api = Api(app)
sslify = SSLify(app)
db.init_app(app)
app.secret_key = "b'z\x8a#\n8\x06\xe2\xd5\xe7\xba\x0c\xbc\xc6\x1d&*'"

# TODO: СКОРРЕКТИРОВАТЬ НАИМЕНОВАНИЕ И ПУТЬ
UPLOAD_FOLDER_PATH = 'static/presentations/'

class AdminService(Resource):

    @app.route('/admin', methods=['GET'])
    def admin():
        if 'username' in session:
            return render_template('admin.html')
        else:
            return redirect(url_for('login'))

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'GET':
            return render_template('login.html')
        elif (request.method == 'POST'):
            username = request.form.get('username')
            password = request.form.get('password')

            if AdminService.checkCredentials('username.txt', username) == 1 and AdminService.checkCredentials('password.txt', password) == 1:
                session['username'] = username
                return redirect(url_for('admin'))
            else:
                error='Неверный логин или пароль'
                return render_template('login.html', error=error)
    
    @app.route('/logout', methods=['POST'])
    def logout():
        session.pop('username')
        return redirect(url_for('login'))

    @app.route('/createPresentation', methods=['GET', 'POST'])
    def createPresentation():
        if 'username' in session:
            if request.method == 'GET':
                return render_template('createPresentation.html')
            elif request.method == 'POST':
                # Get title, description and images from request
                title = request.form.get('title')
                description = request.form.get('description')
                images = AdminService.getImagesFromRequest()
                
                # Generate ID for a new presentation
                newPresentationId = AdminService.getNewPresentationId()

            # Create Presentation Object and it to database
            newPresentation = Presentation(newPresentationId, title, description,
                                            secure_filename(images[0].filename), secure_filename(images[1].filename),
                                            secure_filename(images[2].filename), secure_filename(images[3].filename),
                                            secure_filename(images[4].filename), secure_filename(images[5].filename),
                                            secure_filename(images[6].filename), secure_filename(images[7].filename),
                                            secure_filename(images[0].filename), True)
            AdminService.saveNewPresentationToDb(newPresentation)

            # TODO: ПЕРЕДЕЛАТЬ МЕХАНИКУ СОХРАНЕНИЯ
            # Create new dir and save there images
            AdminService.createPresentationDir(newPresentationId)
            AdminService.savePresentationImagesToDir(images, newPresentationId)

        else:
            return redirect(url_for('login'))

    @app.route('/choosePresentationToUpdate', methods=['GET'])
    def choosePresentationToUpdate():
        if 'username' in session:
            if request.method == 'GET':
                # Получить список презентаций
                data = AdminService.getPresentationsList()
                
                # Мб presentationListSerialized надо будет делать .json, если не будет работать
                return render_template('choosePresentationToUpdate.html', presentationsList=data)
        else:
            return redirect(url_for('login'))

    @app.route('/updatePresentation/<id>', methods=['GET', 'POST'])
    def updatePresentation(id):
        if 'username' in session:
            if request.method == 'GET':
                # Получить карточку презентации (мб надо будет делать .json, если не будет отрабатывать)
                presentation = AdminService.getPresentationById()
                return render_template('updatePresentation.html', data=presentation)
            
            elif request.method == 'POST':
                # Get title, description and images from request
                newTitle = request.form.get('title')
                newDescription = request.form.get('description')
                images = AdminService.getImagesFromRequest()
                presentationToUpdate = Presentation.query.filter_by(id=id)

                # Update title, description, images and commit it
                presentationToUpdate.update(dict(title=newTitle))
                presentationToUpdate.update(dict(description=newDescription))
                
                if images[0].filename != '':
                    presentationToUpdate.update(dict(firstImagePath=secure_filename(images[0].filename)))
                    presentationToUpdate.update(dict(mainImagePath=secure_filename(images[0].filename)))
                if images[1].filename != '':
                    presentationToUpdate.update(dict(secondImagePath=secure_filename(images[1].filename)))
                if images[2].filename != '':
                    presentationToUpdate.update(dict(thirdImagePath=secure_filename(images[2].filename)))
                if images[3].filename != '':
                    presentationToUpdate.update(dict(fourthImagePath=secure_filename(images[3].filename)))
                if images[4].filename != '':
                    presentationToUpdate.update(dict(fifthImagePath=secure_filename(images[4].filename)))
                if images[5].filename != '':
                    presentationToUpdate.update(dict(sixthImagePath=secure_filename(images[5].filename)))
                if images[6].filename != '':
                    presentationToUpdate.update(dict(seventhImagePath=secure_filename(images[6].filename)))
                if images[7].filename != '':
                    presentationToUpdate.update(dict(eightImagePath=secure_filename(images[7].filename)))
                
                db.session.commit()

            AdminService.savePresentationImagesToDir(images, id)

        else:
            return redirect(url_for('login'))

    @app.route('/deletePresentation', methods=['GET', 'POST'])
    def deletePresentation():
        if 'username' in session:
            if request.method == 'GET':
                # Получить список презентаций
                data = AdminService.getPresentationsList()

                return render_template('deletePresentation.html', presentationsList=data)
            elif request.method == 'POST':
                presentationIdsToDelete = request.form.getlist('id')
                for i in range(len(presentationIdsToDelete)):
                    Presentation.query.filter_by(id=presentationIdsToDelete[i]).update(dict(active=False))
                    db.session.commit()
        else:
            return redirect(url_for('login'))

    def checkCredentials(filename, value):
        file = open(filename, 'r')
        if (file.read() == value):
            return 1
        else:
            return 0

    def getPresentationsList():
        presentationsList = Presentation.query.filter_by(active=True).all()
        presentationsListSerialized = []

        for i in presentationsList:
            presentationsListSerialized.append(Presentation.serialize(i))

        return jsonify(presentationsListSerialized)

    def getPresentationById(id):
        presentation = Presentation.query.filter_by(id=id, active=True).first_or_404()
        return Presentation.serialize(presentation)

    def getImagesFromRequest():
        images = []
        filename = 'file'
        for number in range(8):
            fullFilename = filename+str(number)
            images.append(request.files[fullFilename])

        return images

    def getNewPresentationId():
        return AdminService.getMaxId()+1

    def getMaxId():
            presentationsList = Presentation.query.all()
            maxId = 0
            for i in presentationsList:
                if i.id > maxId:
                    maxId = i.id
            return maxId

    def saveNewPresentationToDb(newPresentation):
        db.session.add(newPresentation)
        db.session.commit()

    # Сохранить картинки
    def savePresentationImagesToDir(images, dirId):
        for i in range(len(images)):
            filename = secure_filename(images[i].filename)
            path = UPLOAD_FOLDER_PATH+str(dirId)+'/'+filename
            if os.path.exists(path) != True:
                images[i].save(path)

    def createPresentationDir(id):
        path = UPLOAD_FOLDER_PATH+str(id)
        os.mkdir(path)

api.add_resource(AdminService)
if __name__ == "__main__":
    app.run(debug=True)
