import unittest
from main import book, comic, main
class testing(unittest.TestCase):
    def test_create_book(self):
        test_book = book("test", "test", "test", "test", "test")
        assert test_book.title == "test"
        assert test_book.genre == "test"
        assert test_book.releaseDate == "test"
        assert test_book.author == "test"
        assert test_book.publisher == "test"

    def test_create_comic(self):
        test_comic = comic("test", "test", "test", "test", "test", "test")
        assert test_comic.title == "test"
        assert test_comic.genre == "test"
        assert test_comic.releaseDate == "test"
        assert test_comic.author == "test"
        assert test_comic.publisher == "test"
        assert test_comic.artist == "test"

if __name__ == '__main__':
    # unittest.main()
    main()



"""
Test log: 
For Unit test, create class objects, pass tests.
For main.py test, save() pass the test, load() pass the test, createItem() function has some issues,  
for x in inventory:
            id += 1
            print("ID: ", id)
inventory[id] = book(title, genre, releaseDate, author, publisher)inventory 
inventory was not defined in the function, which cause the error. Either pass it in from a function argument or something else, or this will cause obvious problems.
As for the file saving results, it can accomplish the basic task. However, during testing, I found that it overwrites the previous content and does not add a new entry under unknown circumstances.
There are also some input validation aspects, the program will exit directly after entering incorrectly formatted dates or invalid content, rather than requiring re-input, I think this is an area that needs improvement.
"""