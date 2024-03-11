import json
import os

class Book:
    def __init__(self, title, genre, releaseDate, author, publisher, isbn, id=None):
        self.id = id
        self.title = title
        self.genre = genre
        self.releaseDate = releaseDate
        self.author = author
        self.publisher = publisher
        self.isbn = isbn

class Book_Manager:
    def __init__(self, file_path='inventory.json'):
        self.file_path = file_path # path to the inventory file
        self.books = [] # list of books in the inventory
        if not os.path.exists(self.file_path): # check if the inventory file exists
            self.create_empty_inventory() # create an empty inventory
        self.load_books() # load books from the inventory file

    def create_empty_inventory(self):
        # Create an empty inventory file if it doesn't exist
        try:
            with open(self.file_path, 'w', encoding='utf-8') as file:
                json.dump([], file)  # Save an empty list to signify no books
            print("New inventory created.")
        except IOError as e:
            print(f"Error creating new inventory: {e}")


    def add_book(self, book):
        if self.books:
            max_id = max(book.id for book in self.books) # get the maximum ID in the list
            new_id = max_id + 1 # increment the maximum ID
        else:
            new_id = 1 # if the list is empty, start with ID 1
        book.id = new_id
        self.books.append(book)  # add the book to the list
        self.save_books()  # save changes

    def remove_book(self, book_id):
        book_id = int(book_id)  # convert book_id to an integer
        book_to_remove = None 
        for book in self.books: # loop through the list of books
            if book.id == book_id: # find the book with the matching ID
                book_to_remove = book # set the book to be removed
                break
        if book_to_remove: # if a book was found
            self.books.remove(book_to_remove) # remove the book
            self.save_books()
        else:
            print("Book not found.")

    def find_book(self, search_value, search_by='id'):
        for book in self.books:
            if str(getattr(book, search_by, '')).lower() == str(search_value).lower(): # use getattr to get the value of the search_by attribute
                return book

    def save_books(self):
        with open(self.file_path, 'w', encoding='utf-8') as file: # I set encoding to utf-8 to avoid encoding errors
            json_books = [vars(book) for book in self.books] # convert each book to a dictionary
            json.dump(json_books, file, indent=4) # save the list of books, indented by 4 spaces

    def load_books(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                books_data = json.load(file) # load the list of books
                self.books = [Book(**book_data) for book_data in books_data] # convert each dictionary to a Book object
        except FileNotFoundError:
            print("File not found.") 
        except json.JSONDecodeError:
            print("Invalid JSON data in inventory file.")
    
    def update_book(self, new_book):
        book = self.find_book(new_book.id)
        if book:
            book.title = new_book.title
            book.genre = new_book.genre
            book.releaseDate = new_book.releaseDate
            book.author = new_book.author
            book.publisher = new_book.publisher
            book.isbn = new_book.isbn
            self.save_books()
        else:
            print("Book not found.")
        
