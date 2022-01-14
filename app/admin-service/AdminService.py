# @Author: Daniil Maslov (ComicSphinx)

from flask import Flask, session, redirect, url_for, request, flash
from flask.templating import render_template
from flask_restful import Api, Resource
import requests

app = Flask(__name__)
api = Api(app)
app.secret_key = "b'z\x8a#\n8\x06\xe2\xd5\xe7\xba\x0c\xbc\xc6\x1d&*'"

DB_SERVICE_BASE_URL = 'http://127.0.0.1'

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

            if checkCredentials('username.txt', username) == 1 and checkCredentials('password.txt', password) == 1:
                session['username'] = username
                return redirect(url_for('admin'))
            else:
                error='Неверный логин или пароль'
                return render_template('login.html', error=error)
    
    @app.route('/logout', methods=['POST'])
    def logout():
        session.pop('username')
        return redirect(url_for('login'))

    @app.route('/createPresentation', methods=['POST', 'GET'])
    def createPresentation():
        if 'username' in session:
            if request.method == 'GET':
                return render_template('createPresentation.html')
        else:
            return redirect(url_for('login'))

    @app.route('/updatePresentation', methods=['PUT', 'GET'])
    def updatePresentation():
        if 'username' in session:
            if request.method == 'GET':
                return render_template('updatePresentation.html')
        else:
            return redirect(url_for('login'))

    @app.route('/deletePresentation', methods=['GET'])
    def deletePresentation():
        if 'username' in session:
            if request.method == 'GET':
                # Отправить запрос, получить ответ
                url = DB_SERVICE_BASE_URL+'/getPresentationsListData'
                data = requests.get(url).json()

                return render_template('deletePresentation.html', presentationsList=data)
        else:
            return redirect(url_for('login'))

def checkCredentials(filename, value):
    file = open(filename, 'r')
    if (file.read() == value):
        return 1
    else:
        return 0

api.add_resource(AdminService)
if __name__ == "__main__":
    app.run(debug=True)
