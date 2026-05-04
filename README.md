# Book Alchemy 📚

A web-based library management app built with **Flask** and **SQLAlchemy**. Add authors and books to a personal database, search your collection, sort by title or author, and delete books with automatic author cleanup.

## Features

- ➕ **Add authors** with name, birth date, and optional date of death
- 📖 **Add books** with title, ISBN, publication year, and author (linked via database relationship)
- 🔍 **Search books** by title with live filtering
- 🔃 **Sort** your library by title or author name
- 🗑️ **Delete books** — authors are automatically removed when their last book is deleted
- 💾 **SQLite database** — persistent local storage via SQLAlchemy ORM

## Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat&logo=flask&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=flat&logo=sqlalchemy&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat&logo=sqlite&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white)

## Data Model

```
Author                    Book
──────────────────        ──────────────────────
id (PK)                   id (PK)
name                      title
birth_date                isbn
date_of_death             publication_year
                          author_id (FK → Author)
```

A one-to-many relationship: one author can have many books. Deleting the last book of an author automatically removes the author from the database.

## Project Structure

```
Book-Alchemy/
├── app.py             # Flask routes & application logic
├── data_models.py     # SQLAlchemy models (Author, Book)
├── data/
│   └── library.sqlite # SQLite database (auto-created)
└── templates/
    ├── home.html      # Book list with search & sort
    ├── add_author.html
    └── add_book.html
```

## Getting Started

**1. Clone the repository**
```bash
git clone https://github.com/vincentkoenig/Book-Alchemy.git
cd Book-Alchemy
```

**2. Install dependencies**
```bash
pip install flask flask-sqlalchemy
```

**3. Initialize the database**

Uncomment the following lines at the bottom of `app.py` once, then run:
```python
with app.app_context():
    db.create_all()
```
```bash
python app.py
```
This creates `data/library.sqlite` automatically. Re-comment the lines afterwards.

**4. Open in your browser**
```
http://localhost:5000
```

## What I Learned

- Designing relational database models with SQLAlchemy ORM
- Implementing one-to-many relationships with foreign keys and `db.relationship`
- Using Flask-SQLAlchemy for database queries, filtering, and sorting
- Handling cascading deletes based on related data (auto-remove empty authors)
- Separating data models from application logic across multiple files
