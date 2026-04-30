from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    birth_date = db.Column(db.Date)
    date_of_death = db.Column(db.Date)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'))
    isbn = db.Column(db.Integer)
    title = db.Column(db.String)
    publication_year = db.Column(db.Integer)


