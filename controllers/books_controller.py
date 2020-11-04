from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.book import Book
import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

books_blueprint = Blueprint("books", __name__)


# ----- MVP -----

# INDEX, View all Books along with detail of the Author (name etc)
@books_blueprint.route('/books')
def view_books():
    books = book_repository.select_all()
    return render_template('/books/index.html', all_books = books)

# DELETE
@books_blueprint.route('/books/<id>/delete', methods=["POST"])
def delete_book(id):
    book_repository.delete(id)
    return redirect('/books')

# ----- EXTENSIONS ----- \ * Be able to create a new Book, * View a single Book
@books_blueprint.route('/books', methods=["POST"])
def add_new_book():
    title = request.form['title']
    genre = request.form['genre']
    publisher = request.form['publisher']
    author_id = request.form['author_id']

    author = author_repository.select(author_id)
    book = Book(title, genre, publisher, author)
    book_repository.save(book)
    return redirect('/books')



# SHOW
@books_blueprint.route('/books/<id>', methods=["GET"])
def view_single_book(id):
    book = book_repository.select(id)
    return render_template('/books/view.html', book = book)

# NEW


# CREATE



# ----- ADVANCED EXTENSIONS -----

# EDIT


# UPDATE




