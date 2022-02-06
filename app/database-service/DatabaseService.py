# @Author: Daniil Maslov (ComicSphinx)

from flask_restful import Api, Resource
from werkzeug.utils import secure_filename, send_file
from Models import Presentation, app, db
from flask import jsonify, request, send_file
import os

api = Api(app)
app.secret_key = "b'z\x8a#\n8\x06\xe2\xd5\xe7\xba\x0c\xbc\xc6\x1d&*'"

UPLOAD_FOLDER_PATH = 'static/presentations/'

class DatabaseService(Resource):

    # TODO: надо будет убрать этот метод, а в сервисах переделать на получение файла с помощью os
    @app.route('/getPresentation/<id>/image/<imageFieldName>', methods=['GET'])
    def getImageByPresentationIdAndFieldName(imageFieldName, id):
        if request.method == 'GET':
            presentation = DatabaseService.getPresentation(id)
            filename = presentation.get(imageFieldName)
            path = UPLOAD_FOLDER_PATH+str(id)+'/'+filename
            return send_file(path, mimetype='image/jpeg')