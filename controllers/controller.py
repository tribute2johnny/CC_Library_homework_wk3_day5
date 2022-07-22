from flask import Flask, render_template, request, redirect
from app import app
from modules.book import Book
from modules.book_list import books, add_book, remove_book 

@app.route('/books')
def index():
    return render_template('books.html', title='The Phil Mitchell Library', books=books)

@app.route('/books/new')
def new_book():
    return render_template('new_book.html', title='New Book')

@app.route('/books', methods=['POST'])
def create_book():
    print(request.form)
    title = request.form['title']
    author = request.form['author']
    genre = request.form['genre']
    new_book = Book(title, author, genre)
    add_book(new_book)
    return redirect('/books')

@app.route('/books/delete/<book>', methods=['POST'])
def delete_book_by_index(book):
    remove_book(int(book))
    return redirect('/books')


    