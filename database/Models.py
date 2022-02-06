# @Aurhor: Daniil Maslov (ComicSphinx)

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://gdjqbznobxhqxk:cf39ce62f344cfa9cb15eba8c31a6e0304f42750e5f69a3563da7505f1f80fb5@ec2-3-212-143-188.compute-1.amazonaws.com:5432/d5hggk2n1g9v3n'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class Presentation(db.Model):
    __tablename__ = "Presentation"
    id                  = db.Column(db.Integer, primary_key=True)
    title               = db.Column(db.String, nullable = False)
    description         = db.Column(db.String)
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

    def __init__(self, id, title, description, firstImagePath, secondImagePath, thirdImagePath, fourthImagePath, fifthImagePath, sixthImagePath,
                    seventhImagePath, eightImagePath, mainImagePath, active):
        self.id = id
        self.title = title
        self.description = description
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