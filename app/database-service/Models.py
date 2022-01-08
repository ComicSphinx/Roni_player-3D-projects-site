# @Aurhor: Daniil Maslov (ComicSphinx)

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///main.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class Presentation(db.Model):
    __tablename__ = "Presentation"
    id                  = db.Column(db.Integer, primary_key=True)
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

    def __init__(self, id, title, description, descriptionTitle, firstImagePath, secondImagePath, thirdImagePath, fourthImagePath, fifthImagePath, sixthImagePath,
                    seventhImagePath, eightImagePath, mainImagePath, active):
        self.id = id
        self.title = title
        self.description = description
        self.descriptionTitle = descriptionTitle
        self.firstImagePath = firstImagePath
        self.secondImagePath = secondImagePath
        self.thirdImagePath = thirdImagePath
        self.fourthImagePath = fourthImagePath
        self.fifthImagePath = fifthImagePath
        self.sixthImagePath = sixthImagePath
        self.seventhImagePath = seventhImagePath
        self.eightImagePath = eightImagePath
        self.mainImagePath = mainImagePath
        self.active = active

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'descriptionTitle': self.descriptionTitle,
            'firstImagePath': self.firstImagePath,
            'secondImagePath': self.secondImagePath,
            'thirdImagePath': self.thirdImagePath,
            'fourthImagePath': self.fourthImagePath,
            'fifthImagePath': self.fifthImagePath,
            'sixthImagePath': self.sixthImagePath,
            'seventhImagePath': self.seventhImagePath,
            'eightImagePath': self.eightImagePath,
            'mainImagePath': self.mainImagePath,
            'active': self.active
        }