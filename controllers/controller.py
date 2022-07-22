from flask import Flask, render_template, request, redirect
from app import app
from modules.book import Book
from modules.book_list import books 

@app.route('/books')
def index():
    return render_template('books.html', title='The Phil Mitchell Library', books=books)

