from flask import Flask, render_template, request, redirect
from app import app
from models.book import *
from models.book_list import books, add_book, remove_book 
import datetime

@app.route('/books')
def index():
    return render_template('books.html', title='The Phil Mitchell Library', books=books)

@app.route('/books/new')
def new_book():
    return render_template('new_book.html', title='New Book')

@app.route('/books/<index>')
def view_book(index):
    chosen_book = books[int(index)]
    return render_template('book.html', book=chosen_book)


@app.route('/books', methods=['POST'])
def create_book():
    print(request.form)
    title = request.form['title']
    author = request.form['author']
    genre = request.form['genre']
    return_by = request.form['return_by']
    checked_out = False if 'checked_out' in request.form else True
    split_date = return_by.split('-')
    return_by = datetime.date(int(split_date[0]), int(split_date[1]), int(split_date[2]))
    new_book = Book(title, author, genre, checked_out, return_by)
    add_book(new_book)
    return redirect('/books')

@app.route('/books/delete/<index>', methods=['POST'])
def delete_book_by_index(index):
    remove_book(int(index))
    return redirect('/books')



    