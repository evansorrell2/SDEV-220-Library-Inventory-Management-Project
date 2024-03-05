## Requirements:
##### ~ A GUI that interacts with at least 3 classes (Item, Book, and comic)
##### ~ Must use collections (lists, tuples, arrays, and or dictionaries)
##### ~ Must have no runtime or syntax errors and produce correct results
##### ~ Needs documentation including the proposal, class diagram, and
#####   report of results with sample output

## Plan to Fulfill Requirements:
##### ~ The GUI will have several functions in order to fulfill the requirements:
########## - Add books or comics to the "inventory"
########## - Search for items within inventory with the ability to
##########   filter out comics or books in the search
########## - Remove items from the inventory
##### ~ Will use lists within the items' attributes if it is possible to have multiple of said attribute
########## - This may require additional functionality for displaying these items to avoid errors
##### ~ dictionaries can be used to store items in the "inventory"
##### ~ We have the proposal and class diagram and thus just need reports of results (use unit testing to get these)



###----------|Main Program|----------###
from datetime import datetime
import json
import jsonpickle
from models import book, comic
import os

#####-------------Bo's Work-------------#####
def load_inventory():
    filename = 'inventory.json'
    if not os.path.exists(filename):
        with open(filename, 'w') as file:
            print(f"{filename} not found. Creating a new inventory file.")
            file.write(jsonpickle.encode({}))
            return {}
    else:
        with open(filename) as file:
            return jsonpickle.decode(file.read())
        
def print_inventory(inventory):
    for item_id, item in inventory.items():
        print(f"{item_id}: {item}")

def save_inventory(inventory, filename='inventory.json'):
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
        del inventory[item_id]
        print(f"Item {item_id} removed successfully.")
                


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
        item.author = input("Enter the new author: ")
        item.publisher = input("Enter the new publisher: ")
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

        
def main():
    inventory = load_inventory()
    while True:
        print("\nInventory Management System")
        choice = input("1. Add Item\n2. Update Item \n3. Remove Item\n4. Save and Exit \n5. Print Inventory \n6. View Item Details \nEnter your choice: ")
        if choice == '1':
            add_item(inventory)
        elif choice == '2':
            update_item(inventory)
        elif choice == '3':
            remove_item(inventory)
        elif choice == '4':
            save_inventory(inventory)
            print("Inventory saved. Exiting program.")
            break
        elif choice == '5':
            print_inventory(inventory)
        elif choice == '6':
            view_item_details(inventory)
        else:
            print("Invalid choice.")


if __name__ == '__main__':
    main()


########-----------Bo's Work end-----------########
    



# def createItem():
#     date_format = '%Y-%m-%d'
#     itemType = input("Enter the type of item you wish to enter:")
#     if itemType == "Book":
#         title = input("Enter the title of the book:")
#         genre = input("Enter the genre of the book:")
#         releaseDate = get_date_input()
#         author = input("Enter the author of the book:")
#         publisher = input("Enter the publisher of the book:")
#         id = 0
#         for x in inventory:
#             id += 1
#         inventory[id] = book(title, genre, releaseDate, author, publisher)
#         print("You created a book")
#         save()
#         #print(inventory)
#     elif itemType == "Comic":
#         title = input("Enter the title of the comic:")
#         genre = input("Enter the genre of the comic:")
#         releaseDate = get_date_input()
#         author = input("Enter the author of the comic:")
#         publisher = input("Enter the publisher of the comic:")
#         artist = input("Enter the artist of the comic:")
#         id = 0
#         for x in inventory:
#             id += 1
#         inventory[id] = book(title, genre, releaseDate, author, publisher, artist)
#         print("You created a comic")
#     elif itemType == "quit":
#         print("Stopping process...")
#     else:
#         print("Error: item type not recognized. Please enter either 'Book' or 'Comic'.")
#         createItem()
  
# def save():
#     json_string = jsonpickle.encode(inventory)
#     file = open("inventory.txt", "w")
#     file.write(json_string)
#     file.close()
    
# def load():
#     #Inventory is a dictionary containing the item(in the form of a dict) and it's ID number given
#     #to it when it entered the system
#     #The inventory uses JSON formated text to store the items, the code below opens the 
#     inventoryFile = open("inventory.txt", "a") #creates inventory.txt if it is not already there
#     inventoryFile.close()
#     inventoryFile = open("inventory.txt") #reopens the file to read it
#     inventoryRaw = inventoryFile.read() #inventoryRaw stores the raw string that the txt file holds
#     inventoryFile.close()
#     if not (len(inventoryRaw) == 0): #checks if the file is empty, like if it was just created
#         print("Inventory loaded")
#         inventory = json.loads(inventoryRaw) # loads the inventory
#         # A the moment this load is extremely simple and isn't truely readable yet.
#         # ----------Insert load loop here----------
#         print(inventory)
#     else:
#         print("No inventory detected")
#         print("Initializing inventory")
#         inventory = {} #initializes the inventory

#id1 = book("The Hobbit", "High Fantasy", (datetime.datetime(1937, 9, 21)).strftime("%x"), "J. R. R. Tolkien", "George Allen & Unwin")

#inventory[1] = jsonpickle.encode(id1)
#inventoryFile = open("inventory.txt", "w")
#inventoryFile.write(json.dumps(inventory))
#inventoryFile.close()
