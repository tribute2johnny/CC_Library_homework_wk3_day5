import unittest

import datetime

from models.book import *




class TestBook(unittest.TestCase):

        def test_book_has_title(self):
            self.book = Book("The Blood of Elves", "Andrzej Sapkowski", "Fantasy", True, datetime.date(2022, 10, 2))
            self.assertEqual("The Blood of Elves", self.book.title)

        def test_book_has_author(self):
            self.book = Book("The Blood of Elves", "Andrzej Sapkowski", "Fantasy", True, datetime.date(2022, 10, 2))
            self.assertEqual("Andrzej Sapkowski", self.book.author)

        def test_book_has_genre(self):
            self.book = Book("The Blood of Elves", "Andrzej Sapkowski", "Fantasy", True, datetime.date(2022, 10, 2))
            self.assertEqual("Fantasy", self.book.genre)

        def test_book_checked_out(self):
            self.book = Book("The Blood of Elves", "Andrzej Sapkowski", "Fantasy", True, datetime.date(2022, 10, 2))
            self.assertEqual(True, self.book.checked_out)

        def test_book_in_stock(self):
            self.book = Book("The Blood of Elves", "Andrzej Sapkowski", "Fantasy", False, datetime.date(2022, 10, 2))
            self.assertEqual(False, self.book.checked_out)

        def test_checked_out_book_has_return_by(self):
            self.book = Book("The Blood of Elves", "Andrzej Sapkowski", "Fantasy", True, datetime.date(2022, 10, 2))
            self.assertEqual(datetime.date(2022, 10, 2), self.book.return_by)