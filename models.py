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
        self.file_path = file_path
        self.books = []
        if not os.path.exists(self.file_path): 
            self.create_empty_inventory()
        self.load_books()

    def create_empty_inventory(self):
        # Create an empty inventory file if it doesn't exist
        try:
            with open(self.file_path, 'w', encoding='utf-8') as file:
                json.dump([], file)  # Save an empty list to signify no books
            print("New inventory created.")
        except IOError as e:
            print(f"Error creating new inventory: {e}")

    
    def add_book(self, book):
        """Adds a new book to the inventory."""
        if self.books:
            max_id = max(book.id for book in self.books)
            new_id = max_id + 1
        else:
            new_id = 1
        book.id = new_id
        self.books.append(book)  # Add the book to the list
        self.save_books()  # Save changes

    def remove_book(self, book_id):
        book_id = int(book_id)
        book_to_remove = None
        for book in self.books:
            if book.id == book_id:
                book_to_remove = book
                break
        if book_to_remove:
            self.books.remove(book_to_remove)
            self.save_books()
        else:
            print("Book not found.")

    def find_book(self, search_value, search_by='id'):
        """Finds a book in the inventory by a given attribute."""
        books=[]
        for book in self.books:
            if str(getattr(book, search_by, '')).lower() == str(search_value).lower():
                books.append(book)
        return books

    def save_books(self):
        """Saves the current state of the books to the inventory file."""
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json_books = [vars(book) for book in self.books]
            json.dump(json_books, file, indent=4)

    def load_books(self):
        """Loads books from the inventory file."""
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                books_data = json.load(file)
                self.books = [Book(**book_data) for book_data in books_data]
        except FileNotFoundError:
            print("File not found.")  # Handled by the check in __init__
        except json.JSONDecodeError:
            print("Invalid JSON data in inventory file.")

