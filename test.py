import unittest
from models import Book, Book_Manager
import os
class TestBookManager(unittest.TestCase):
    def setUp(self):
        self.test_file_path = 'test_inventory.json'
        self.manager = Book_Manager(file_path=self.test_file_path)
        self.sample_book = Book("Sample Title", "Fiction", "2020-01-01", "Author Name", "Publisher Name", "1234567890")
        self.manager.add_book(self.sample_book)
        
    def tearDown(self):
        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)

    def test_add_book(self):
        new_book = Book("New Book", "Non-Fiction", "2021-02-02", "New Author", "New Publisher", "0987654321f21")
        self.manager.add_book(new_book)
        self.assertEqual(len(self.manager.books), 2)

    def test_remove_book(self):
        self.manager.remove_book(1)
        self.assertEqual(len(self.manager.books), 0)

    def test_find_book(self):
        found_books = self.manager.find_book("Sample Title", search_by='title')
        self.assertEqual(len(found_books), 1)
        self.assertEqual(found_books[0].title, "Sample Title")

    def test_save_and_load_books(self):
        another_book = Book("Another Book", "Drama", "2022-03-03", "Another Author", "Another Publisher", "1122423355")
        self.manager.add_book(another_book)
        self.manager.save_books()

        new_manager = Book_Manager(file_path=self.test_file_path)
        new_manager.load_books()
        self.assertEqual(len(new_manager.books), 2)

if __name__ == '__main__':
    unittest.main()
