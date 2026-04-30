from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from data_models import db, Author, Book
import os
app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'data/library.sqlite')}"
db.init_app(app)


@app.route('/add_author', methods=['GET', 'POST'])
def add_author():
  if request.method == 'GET':
    return render_template('add_author.html')
  else:
    name = request.form.get('name')
    birth_date = request.form.get('birth_date')
    date_of_death = request.form.get('date_of_death')
    new_author = Author(name=name, birth_date=birth_date, date_of_death=date_of_death)
    db.session.add(new_author)
    db.session.commit()

    return render_template('add_author.html', success="Author successfully added!")

@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
  if request.method == 'GET':
    authors = Author.query.all()
    return render_template('add_book.html', authors=authors)
  else:
    author_id = request.form.get('author_id')
    isbn = request.form.get('isbn')
    title = request.form.get('title')
    publication_year = request.form.get('publication_year')

    new_book = Book(author_id=author_id, isbn=isbn, title=title, publication_year=publication_year)
    db.session.add(new_book)
    db.session.commit()

    return render_template('add_book.html', authors=Author.query.all(), success="Book successfully added!")




#with app.app_context():
  #db.create_all()