import os
from sqlalchemy import Column, String, Integer, Date, create_engine
from flask_sqlalchemy import SQLAlchemy 
import json
from settings import DB_NAME, DB_USER, DB_PASSWORD
from flask_migrate import Migrate


database_name= DB_NAME 
database_path = os.environ['DATABASE_URL']
if(database_path != ""):
    if database_path.startswith("postgres://"):
        database_path = database_path.replace("postgres://", "postgresql://", 1)
else:
    database_path = 'postgresql://{}:{}@{}/{}'.format(DB_USER,DB_PASSWORD,'localhost:5432', database_name)


db = SQLAlchemy()

class Models:
    """
    setup_db(app)
        binds a flask application and a SQLAlchemy service
    """
    @staticmethod
    def setup_db(app, database_path=database_path):
        with app.app_context():
            app.config["SQLALCHEMY_DATABASE_URI"] = database_path
            app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
            db.app = app
            db.init_app(app)
            db.create_all()
            Migrate(app, db)

    class Movies(db.Model):
        __tablename__ = 'movies'

        id = Column(Integer, primary_key=True)
        title = Column(String)
        release_date = Column(Date)

        def __init__(self, title, release_date):
            self.title = title
            self.release_date = release_date

        def insert(self):
            db.session.add(self)
            db.session.commit()

        def update(self):
            db.session.commit()

        def delete(self):
            db.session.delete(self)
            db.session.commit()

        def format(self):
            return {
                'id': self.id,
                'title': self.title,
                'release_date': self.release_date.isoformat()
                }

    class Actors(db.Model):
        __tablename__ = 'actors'

        id = Column(Integer, primary_key=True)
        name = Column(String)
        age = Column(Integer)
        gender = Column(String)

        def __init__(self, name, age, gender):
            self.name = name
            self.age = age
            self.gender = gender

        def insert(self):
            db.session.add(self)
            db.session.commit()

        def update(self):
            db.session.commit()

        def delete(self):
            db.session.delete(self)
            db.session.commit()

        def format(self):
            return {
                'id': self.id,
                'name': self.name,
                'age': self.age,
                'gender': self.gender
                }
