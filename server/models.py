from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData()

db = SQLAlchemy(metadata=metadata)


class Pet(db.Model, SerializerMixin):import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Pet(db.Model, SerializerMixin):
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    species = db.Column(db.String)

    def __repr__(self):
        logger.info(f'Pet object created: {self.id}, {self.name}, {self.species}')
        return f'<Pet {self.id}, {self.name}, {self.species}>'

    def __init__(self, name, species):
        self.name = name
        self.species = species
        logger.info(f'Pet object initialized: {self.id}, {self.name}, {self.species}')

    def save(self):
        db.session.add(self)
        db.session.commit()
        logger.info(f'Pet object saved: {self.id}, {self.name}, {self.species}')

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        logger.info(f'Pet object deleted: {self.id}, {self.name}, {self.species}')
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    species = db.Column(db.String)

    def __repr__(self):
        return f'<Pet {self.id}, {self.name}, {self.species}>'
