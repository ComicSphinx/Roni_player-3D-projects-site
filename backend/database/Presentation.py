from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///main.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class Presentation(db.Model):
    presentationId      = db.Column(db.Integer, primary_key=True)
    title               = db.Column(db.String, nullable = False)
    description         = db.Column(db.String)
    descriptionTitle    = db.Column(db.String, nullable = False)
    firstImagePath      = db.Column(db.String, nullable = False)
    secondImagePath     = db.Column(db.String, nullable = False)
    thirdImagePath      = db.Column(db.String, nullable = False)
    fourthImagePath     = db.Column(db.String, nullable = False)
    fifthImagePath      = db.Column(db.String, nullable = False)
    sixthImagePath      = db.Column(db.String, nullable = False)
    seventhImagePath    = db.Column(db.String, nullable = False)
    eightImagePath      = db.Column(db.String, nullable = False)
    mainImagePath       = db.Column(db.String, nullable = False)
    active              = db.Column(db.Boolean, nullable = False)