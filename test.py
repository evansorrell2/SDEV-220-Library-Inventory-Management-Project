import unittest
from models import book, comic

class TestModels(unittest.TestCase):
    def test_book_creation(self):
        '''Test book creation'''
        b = book('Test title', 'Test genre', '2022-01-01', 'Test author', 'Test publisher')
        self.assertEqual(b.title, 'Test title')
        self.assertEqual(b.author, 'Test author')

    def test_comic_creation(self):
        '''Test comic creation'''
        c = comic('Test title', 'Test genre', '2022-01-01', 'Test author', 'Test publisher', 'Test artist')
        self.assertEqual(c.title, 'Test title')
        self.assertEqual(c.artist, 'Test artist')

if __name__ == '__main__':
    unittest.main()
