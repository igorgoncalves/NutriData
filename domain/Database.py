from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///dados.db', echo=True)
db = declarative_base()
db.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

