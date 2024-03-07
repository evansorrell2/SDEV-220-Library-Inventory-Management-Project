import tkinter as tk
from tkinter import simpledialog, messagebox, scrolledtext
import jsonpickle
import os
from datetime import datetime

def print_inventory(inventory):
    for item_id, item in inventory.items():
        print(f"{item_id}: {item}")

def save_inventory(inventory):
    filename='inventory.json'
    with open(filename, 'w') as file:
        file.write(jsonpickle.encode(inventory))


def get_date_input():
    while True:
        dateInput = input("Enter the release date (YYYY-MM-DD): ")
        try:
            return datetime.strptime(dateInput, '%Y-%m-%d').strftime("%Y-%m-%d")
        except ValueError as e:
            print("Invalid date format. Please try again using YYYY-MM-DD.")

def create_item():
    while True:
        print("Choose the type of item to create:")
        print("1. Book\n2. Comic \n3. Quit")
        choice = input("Enter your choice: ")
        if choice == '3':
            print("Exiting item creation.")
            return None
        
        title = input("Enter the title: ")
        genre = input("Enter the genre: ")
        releaseDate = get_date_input()

        if choice == '1'or choice == '2':
            author = input("Enter the author: ")
            publisher = input("Enter the publisher: ")
            if choice == '1':
                return book(title, genre, releaseDate, author, publisher)
            elif choice == '2':
                artist = input("Enter the artist: ")
                return comic(title, genre, releaseDate, author, publisher, artist)
        else:
            print("Invalid choice. Please try again.")
            continue

def add_item(inventory):
    item = create_item()
    if item:
        if inventory:
            # if the inventory is not empty, get the maximum ID
            max_id = max(map(int, inventory.keys()))
            item_id = max_id + 1
        else:
            # if the inventory is empty, start with ID 1
            item_id = 1
        inventory[str(item_id)] = item 
        print(f"Item '{item.title}' added successfully with ID {item_id}.")
    else:
        print("Item creation cancelled.")


def remove_item(inventory):
    if not inventory:
        print("Inventory is empty.")
        return

    item_id, _ = find_item_by_id_or_title(inventory)
    if item_id and item_id in inventory:
        decision = input(f"Are you sure you want to remove item {item_id}? (y/n): ")
        if decision.lower() == 'y':
            del inventory[item_id]
            print(f"Item {item_id} removed successfully.")
        else:
            print("Item removal cancelled.")
            return
                


def update_item(inventory):
    if not inventory:
        print("Inventory is empty.")
        return
    
    item_id, item = find_item_by_id_or_title(inventory)
    if item:
        update_item_attribute(item)
        print(f"Item {item_id} updated successfully.")


def find_item_by_id_or_title(inventory):
    identifier = input("Enter the ID or title of the item to search: ")
    if identifier in inventory:
        return identifier, inventory[identifier]
    
    results = search_item(inventory, identifier)
    if not results:
        print("Item not found.")
        return None, None
    
    if len(results) == 1:
        return results[0]
    
    for index, item in enumerate(results):
        print(f"{index+1}. ID: {item[0]}, Title: {item[1].title}")

    while True:
        choice = input("Enter the number of the item: ")
        if choice.isdigit() and 1 <= int(choice) <= len(results):
            return results[int(choice) - 1]
        else:
            print("Invalid choice. Please enter a valid number.")


def search_item(inventory, search_term):
    results = []
    for item_id, item in inventory.items():
        if search_term.lower() in item.title.lower():
            results.append((item_id, item))
    return None if not results else results


def update_item_attribute(item):
    item.title = input("Enter the new title: ")
    item.genre = input("Enter the new genre: ")
    item.releaseDate = get_date_input()
    item.author = input("Enter the new author: ")
    item.publisher = input("Enter the new publisher: ")
        
    if isinstance(item, comic):
        item.artist = input("Enter the new artist: ")
    else:
        print(f"Update operation for {type(item).__name__} not supported.")

def display_item_details(item):
    print("\nItem Details:")
    print(f"Title: {item.title}")
    print(f"Genre: {item.genre}")
    print(f"Release Date: {item.releaseDate}")
    if isinstance(item, book):
        print(f"Author: {item.author}")
        print(f"Publisher: {item.publisher}")
        if isinstance(item, comic):
            print(f"Artist: {item.artist}")
    print("\n")


def view_item_details(inventory):
    item_id, item = find_item_by_id_or_title(inventory)
    if item:
        display_item_details(item)
    else:
        print("No item found with the given ID or title.")

def load_inventory():
    filename = 'inventory.json'
    if not os.path.exists(filename):
        with open(filename, 'w') as file:
            file.write(jsonpickle.encode({}))
        return {}
    else:
        with open(filename, 'r') as file:
            return jsonpickle.decode(file.read())
class inventoryApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.inventory = load_inventory()
        self.title("Fixed Size Window")
        self.geometry("800x600+600+500")
        self.resizable(True, True)
        self.minsize(800, 600)
        self.create_widgets()

        # label = tk.Label(self, text="This is a fixed size window")
        # label.pack(pady = 20)

    def create_widgets(self):
        self.main_menu_frame = tk.Frame(self)
        self.main_menu_frame.pack(fill="both", expand=True)

        self.main_menu_frame.grid_columnconfigure(0, weight=1)
        self.main_menu_frame.grid_columnconfigure(1, weight=1)
        self.main_menu_frame.grid_columnconfigure(2, weight=1)
        self.main_menu_frame.grid_columnconfigure(3, weight=1)

        add_button = tk.Button(self.main_menu_frame, text="Add Item", command=self.add_item)
        # add_button.pack(pady=10)
        add_button.grid(row=0, column=0, sticky='ew', padx=10, pady=20)
        
        search_button = tk.Button(self.main_menu_frame, text="Search Item", command=self.search_item)
        # search_button.pack(pady=10)
        search_button.grid(row=0, column=1, sticky='ew', padx=10, pady=20)
        
        update_button = tk.Button(self.main_menu_frame, text="Update Item", command=self.update_item)
        # update_button.pack(pady=10)
        update_button.grid(row=0, column=2, sticky='ew', padx=10, pady=20)
        
        delete_button = tk.Button(self.main_menu_frame, text="Delete Item", command=self.delete_item)
        # delete_button.pack(pady=10)
        delete_button.grid(row=0, column=3, sticky='ew', padx=10, pady=20)

        self.inventory_display = scrolledtext.ScrolledText(self, height = 20, width = 50)
        self.inventory_display.pack(pady=10, fill="both", expand=True)

        print_inv_button = tk.Button(self, text="Print Inventory", command=self.print_inventory)
        print_inv_button.pack(pady=10)

    def hide_main_menu(self):
        self.main_menu_frame.pack_forget()

    def show_main_menu(self):
        self.main_menu_frame.pack(fill="both", expand=True)

    def add_item(self):
        self.hide_main_menu()
        messagebox.showinfo("Add Item")
        self.add_window = tk.Toplevel(self)
        self.add_window.title("Add New Item")

        tk.Label(self.add_window, text="Title:").pack()
        self.title_entry = tk.Entry(self.add_window)
        self.title_entry.pack()

        tk.Label(self.add_window, text="Genre:").pack()
        self.genre_entry = tk.Entry(self.add_window)
        self.genre_entry.pack()

        tk.Label(self.add_window, text="Release Date (YYYY-MM-DD):").pack()
        self.release_date_entry = tk.Entry(self.add_window)
        self.release_date_entry.pack()

        tk.Button(self.add_window, text="Submit", command=self.submit_item).pack()
        
        return_button = tk.Button(self.add_window, text="Return to Main Menu", command=self.show_main_menu)
        return_button.pack()


    def submit_item(self):
        title = self.title_entry.get()
        genre = self.genre_entry.get()
        release_date = self.release_date_entry.get()
        if not(title and genre and release_date):
            messagebox.showerror("Error", "Please fill in all fields.", parent=self.add_window)
            return
        new_item = {"title": title, "genre": genre, "releaseDate": release_date}
        item_id = len(self.inventory) + 1
        self.inventory[item_id] = new_item

        messagebox.showinfo("Success", "Item added successfully.", parent=self.add_window)
        self.add_window.destroy()

    def search_item(self):
        self.hide_main_menu()
        messagebox.showinfo("Search Item")

    def update_item(self):
        messagebox.showinfo("Update Item")

    def delete_item(self):
        messagebox.showinfo("Delete Item")
    
    def print_inventory(self):
        self.inventory_display.delete("1.0", tk.END)
        for item_id, item in self.inventory.items():
            item_info = f"{item_id}: {item}"
            self.inventory_display.insert(tk.END, item_info)

    def show_main_menu(self):
        self.main_menu_frame.pack(fill="both", expand=True)

class item:
    def __init__(self, title, genre, releaseDate):
        self.title = title
        self.genre = genre
        self.releaseDate = releaseDate
        
    def __str__(self):
        return f"{self.title}({self.genre})({self.releaseDate})"
    
    def getTitle(self):
        return self.title
    
    def getGenre(self):
        return self.genre
    
    def getReleaseDate(self):
        return self.releaseDate
    
    
class book(item):
    def __init__(self, title, genre, releaseDate, author, publisher):
        super().__init__(title, genre, releaseDate)
        self.author = author
        self.publisher = publisher
        
    def getAuthor(self):
        return self.author
    
    def getPublisher(self):
        return self.publisher
    

    
class comic(book):
    def __init__(self, title, genre, releaseDate, author, publisher, artist):
        super().__init__(title, genre, releaseDate, author, publisher)
        self.artist = artist
        
    def getArtist(self):
        return self.artist
    
'''
class movie(item):
    def __init__(self, title, genre, releaseDate, runtime, maturityRating, qualityRating, cast, director, producer):
        super().__init__(title, genre, releaseDate)
        self.runtime = runtime
        self.maturityRating = maturityRating
        self.qualityRating = qualityRating
        self.cast = cast
        self.director = director
        self.producer = producer
        
    def getRuntime(self):
        return self.runtime
    def getMaturityRating(self):
        return self.maturityRating
    def getQualityRating(self):
        return self.qualityRating
    def getCast(self):
        return self.cast
    def getDirector(self):
        return self.director
    def getProducer(self):
        return self.producer
    
class show(movie):
    def __init__(self, title, genre, releaseDate, runtime, maturityRating, qualityRating, cast, director, producer, season, numEpisodes):
        super().__init__(title, genre, releaseDate, runtime, maturityRating, qualityRating, cast, director, producer)
        self.season = season
        self.numEpisodes = numEpisodes
        
    def getSeason(self):
        return self.season
    def getNumEpisodes(self):
        return self.numEpisodes
    
class game(item):
    def __init__(self, title, genre, releaseDate, numPlayers, playingTime, publisher):
        super().__init__(title, genre, releaseDate)
        self.numPlayers = numPlayers
        self.playingTime = playingTime
        self.publisher = publisher
        
    def getNumPlayers(self):
        return self.numPlayers
    def getPlayingTime(self):
        return self.playingTime
    def getPublisher(self):
        return self.publisher
    
class videoGame(game):
    def __init__(self, title, genre, releaseDate, numPlayers, playingTime, publisher, gameType, platform, esrbRating, qualityRating, cast, developer):
        super().__init__(title, genre, releaseDate, numPlayers, playingTime, publisher)
        self.gameType = gameType
        self.platform = platform
        self.esrbRating = esrbRating
        self.qualityRating = qualityRating
        self.cast = cast
        self.developer = developer
        
    def getGameType(self):
        return self.gameType
    def getPlatform(self):
        return self.platform
    def getEsrbRating(self):
        return self.esrbRating
    def getQualityRating(self):
        return self.qualityRating
    def getCast(self):
        return self.cast
    def getDeveloper(self):
        return self.developer
    
class boardGame(game):
    def __init__(self, title, genre, releaseDate, numPlayers, playingTime, publisher, gameFormat, designer, artist):
        super().__init__(title, genre, releaseDate, numPlayers, playingTime, publisher)
        self.gameFormat = gameFormat
        self.designer = designer
        self.artist = artist
        
    def getGameFormat(self):
        return self.gameFormat
    def getDesigner(self):
        return self.designer
    def getArtist(self):
        return self.artist

'''