from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from data_models import db, Author, Book
import os
from datetime import datetime
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
    try:
        birth_date = datetime.strptime(request.form.get('birth_date'), '%Y-%m-%d').date()
        date_of_death = request.form.get('date_of_death')
        date_of_death = datetime.strptime(date_of_death, '%Y-%m-%d').date() if date_of_death else None
    except ValueError:
        return render_template('add_author.html', error="Invalid date format!")


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
    if not title or not isbn or not author_id:
        return render_template('add_book.html', authors=Author.query.all(), error="Book could not be added!")
    try:
        publication_year = int(request.form.get('publication_year'))
    except ValueError:
        return render_template('add_book.html', authors=Author.query.all(), error="Not a valid year!")


    new_book = Book(author_id=author_id, isbn=isbn, title=title, publication_year=publication_year)
    db.session.add(new_book)
    db.session.commit()

    return render_template('add_book.html', authors=Author.query.all(), success="Book successfully added!")


@app.route('/')
def home():
    sort_by = request.args.get('sort_by', 'title')
    search = request.args.get('search', '')
    message = request.args.get('message', '')

    if search:
        books = Book.query.filter(Book.title.like(f'%{search}%')).all()
    elif sort_by == 'author':
        books = Book.query.join(Author).order_by(Author.name).all()
    else:
        books = Book.query.order_by(Book.title).all()

    if search and not books:
        message = "No books found matching your search."

    return render_template('home.html', books=books, sort_by=sort_by, message=message)


@app.route('/book/<int:book_id>/delete', methods=['POST'])
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    author = book.author

    db.session.delete(book)
    db.session.commit()

    # Delete author if no more books
    if len(author.books) == 0:
        db.session.delete(author)
        db.session.commit()

    return redirect(url_for('home', message="Book successfully deleted!"))

if __name__ == '__main__':
    app.run(debug=True)



#with app.app_context():
  #db.create_all()