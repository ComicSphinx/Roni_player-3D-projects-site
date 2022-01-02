from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.sqltypes import Boolean

# Starting point
engine = create_engine('sqlite:///main.db')
base = declarative_base()

class Presentations(base):
    __tablename__       = "Presentations"
    presentationId      = Column(Integer, primary_key=True)
    title               = Column(String)
    description         = Column(String)
    descriptionTitle    = Column(String)
    firstImagePath      = Column(String)
    secondImagePath     = Column(String)
    thirdImagePath      = Column(String)
    fourthImagePath     = Column(String)
    fifthImagePath      = Column(String)
    sixthImagePath      = Column(String)
    seventhImagePath    = Column(String)
    eightImagePath      = Column(String)
    mainImagePath       = Column(String)
    active              = Column(Boolean)

# Map presentations class to the cars table
base.metadata.bind = engine
# Create configured tables
base.metadata.create_all()