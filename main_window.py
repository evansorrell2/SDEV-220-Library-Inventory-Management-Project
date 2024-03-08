import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from models import Book, Book_Manager
from datetime import datetime

class MainWindow:
    def __init__(self, root):
        self.root = root 
        self.book_manager = Book_Manager()  # Create an instance of the Book_Manager

        self.root.title("Library Management System")
        self.root.geometry("800x600-800+400") # I set the position of the window based on my monitor
        self.root.resizable(True, True)  # allow the window to be resized

        self.last_sort_column = None
        self.sort_order = False  # true for ascending, false for descending

        # Create the main frame
        self.main_frame = ttk.Frame(self.root)  # Corrected parent to self.root
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.setup_ui()

    def setup_ui(self):
        self.label = tk.Label(self.main_frame, text="Library Management System")
        self.label.pack()
        
        # Setup the columns for the Treeview
        self.book_list = ttk.Treeview(self.main_frame, columns=("ID", "Title", "Genre", "Release Date", "Author", "Publisher", "ISBN"), show="headings")
        for col in self.book_list['columns']:
            self.book_list.heading(col, text=col.replace("_", " "),command=lambda _col=col: self.treeview_sort_column(_col, False)) 
            self.book_list.column(col, width=100)  # Adjust column widths
        self.book_list.pack(fill=tk.BOTH, expand=True)

        # Button to Add a New Book
        add_button = tk.Button(self.root, text="Add Book", command=self.add_book)
        add_button.pack(side=tk.LEFT, padx=(10, 0), pady=(10, 10))

        # Button to Remove a Book
        remove_button = tk.Button(self.root, text="Remove Book", command=self.remove_book)
        remove_button.pack(side=tk.LEFT, padx=(10, 0), pady=(10, 10))

        # Button to Update a Book
        update_button = tk.Button(self.root, text="Update Book", command=self.update_book)
        update_button.pack(side=tk.LEFT, padx=(10, 0), pady=(10, 10))

        # Button to Search for a Book
        search_button = tk.Button(self.root, text="Search Book", command=self.search_book)
        search_button.pack(side=tk.LEFT, padx=(10, 0), pady=(10, 10))

        self.load_books()

    @staticmethod
    def is_valid_date(date_string):
        try:
            datetime.strptime(date_string, '%Y-%m-%d')
            return True
        except ValueError:
            return False
        
    @staticmethod
    def is_valid_isbn(isbn):
        return len(isbn) in [10, 13]
    
    def add_book(self):
        title = simpledialog.askstring("Add Book", "Enter the title of the book:", parent=self.root)
        genre = simpledialog.askstring("Add Book", "Enter the genre of the book:", parent=self.root)
        release_date = simpledialog.askstring("Add Book", "Enter the release date of the book (YYYY-MM-DD):", parent=self.root)
        author = simpledialog.askstring("Add Book", "Enter the author of the book:", parent=self.root)
        publisher = simpledialog.askstring("Add Book", "Enter the publisher of the book:", parent=self.root)
        isbn = simpledialog.askstring("Add Book", "Enter the ISBN of the book:", parent=self.root)

        # Validate the input
        if not all([title, genre, release_date, author, publisher, isbn]):
            messagebox.showerror("Error", "Please enter all required fields.", parent=self.root)
            return

        if not self.is_valid_date(release_date):
            messagebox.showerror("Error", "Invalid date format. Please enter the date in YYYY-MM-DD format.", parent=self.root)
            return

        if not self.is_valid_isbn(isbn):
            messagebox.showerror("Error", "Invalid ISBN. ISBN should be 10 or 13 characters long.", parent=self.root)
            return

        book = Book(title, genre, release_date, author, publisher, isbn)
        self.book_manager.add_book(book)
        self.load_books()

    def remove_book(self): # remove the selected book
        selected_items = self.book_list.selection() 
        if selected_items:
            confirm = messagebox.askyesno("Confirm", "Are you sure you want to remove the selected book(s)?", parent=self.root)
            if confirm:
                for selected_item in selected_items:
                    book_id = self.book_list.item(selected_item)['values'][0]
                    self.book_manager.remove_book(book_id)
                self.load_books()


    def update_book(self):
        selected_items = self.book_list.selection()
        if selected_items:
            for selected_item in selected_items:
                book_id = self.book_list.item(selected_item)['values'][0]
                book = self.book_manager.find_book(book_id)
                if book:
                    new_title = simpledialog.askstring("Update Book", "Enter the new title:",parent=self.root)
                    new_genre = simpledialog.askstring("Update Book", "Enter the new genre:",parent=self.root)
                    new_release_date = simpledialog.askstring("Update Book", "Enter the new release date:",parent=self.root)
                    new_author = simpledialog.askstring("Update Book", "Enter the new author:",parent=self.root)
                    new_publisher = simpledialog.askstring("Update Book", "Enter the new publisher:",parent=self.root)
                    new_isbn = simpledialog.askstring("Update Book", "Enter the new ISBN:",parent=self.root)
                    if new_title:
                        book.title = new_title
                    if new_genre:
                        book.genre = new_genre
                    if new_release_date:
                        book.releaseDate = new_release_date
                    if new_author:
                        book.author = new_author
                    if new_publisher:
                        book.publisher = new_publisher
                    if new_isbn:
                        book.isbn = new_isbn
                    self.book_manager.save_books()
                    self.load_books()
                
    def search_book(self):
        search_value = simpledialog.askstring("Search Book", "Enter the title of the book:", parent=self.root)
        if search_value:
            found_books = self.book_manager.find_book(search_value, search_by='title')
            if found_books:
                books_info = "\n\n".join([f"ID: {book.id}\nTitle: {book.title}\nGenre: {book.genre}\nRelease Date: {book.releaseDate}\nAuthor: {book.author}\nPublisher: {book.publisher}\nISBN: {book.isbn}" for book in found_books])
                messagebox.showinfo("Book Information", books_info, parent=self.root)
            else:
                messagebox.showinfo("Book Not Found", "No book found with that title.", parent=self.root)

    def load_books(self):
        for book in self.book_list.get_children():
            self.book_list.delete(book)
        for book in self.book_manager.books:
            self.book_list.insert("", "end", values=(book.id, book.title, book.genre, book.releaseDate, book.author, book.publisher, book.isbn))

    def treeview_sort_column(self,col,reverse): # sort the treeview column
        l = [(self.book_list.set(k, col), k) for k in self.book_list.get_children('')
            if self.book_list.parent(k) == '']
        try:
            l.sort(key = lambda t:int(t[0]),reverse=reverse) # sort by int is for ID column
        except ValueError:
            l.sort(reverse=reverse)

        for index, (val, k) in enumerate(l):
            self.book_list.move(k, '', index)

        self.book_list.heading(col, command=lambda: self.treeview_sort_column(col, not reverse))
        self.last_sort_column = col
        self.sort_order = not reverse  # toggle the sort order