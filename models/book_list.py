from datetime import datetime
from models.book import Book
import datetime

book_1 = Book("The Blood of Elves", "Andrzej Sapkowski", "Fantasy", True, datetime.date(2022, 10, 2))
book_2 = Book("Enemy of God", "Bernard Cornwell", "Fantasy", False, datetime.date(2022, 10, 17))
book_3 = Book("Metro 2033", "Dimitry Glukhovsky", "Post-Apocalyptic", True, datetime.date(2022, 10, 8))
book_4 = Book("1984", "George Orwell", "Science Fiction", False, datetime.date(2022, 10, 2))
book_5 = Book("Leviathan Wakes", "James S. A. Corey", "Science Fiction", False, datetime.date(2022, 10, 9))
book_6 = Book("The Art of War", "Sun Tzu", "Treatise on war", False, datetime.date(2022, 10, 21))
book_7 = Book("Dune", "Frank Herbert", "Science Fiction", True, datetime.date(2022, 10, 2))
book_8 = Book("Cosmos", "Carl Sagan", "Science", False, datetime.date(2022, 10, 7))

books = [book_1, book_2, book_3, book_4, book_5, book_6, book_7, book_8]

def add_book(book):
    books.append(book)

def remove_book(book):
    books.pop(book)