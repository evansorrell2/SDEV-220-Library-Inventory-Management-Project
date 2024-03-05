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

def createItem():
    date_format = '%Y-%m-%d'
    itemType = input("Enter the type of item you wish to enter:")
    if itemType == "Book":
        title = input("Enter the title of the book:")
        genre = input("Enter the genre of the book:")
        year = input("Enter the year of the book's release:")
        month = input("Enter the month of the book's release:")
        day = input("Enter the day of the book's release:")
        releaseDate = (datetime(int(year), int(month), int(day))).strftime("%x")
        author = input("Enter the author of the book:")
        publisher = input("Enter the publisher of the book:")
        id = 0
        for x in inventory:
            id += 1
        inventory[id] = book(title, genre, releaseDate, author, publisher)
        print("You created a book")
        save()
        #print(inventory)
    elif itemType == "Comic":
        title = input("Enter the title of the comic:")
        genre = input("Enter the genre of the comic:")
        year = input("Enter the year of the comic's release:")
        month = input("Enter the month of the comic's release:")
        day = input("Enter the day of the comic's release:")
        releaseDate = (datetime(int(year), int(month), int(day))).strftime("%x")
        author = input("Enter the author of the comic:")
        publisher = input("Enter the publisher of the comic:")
        artist = input("Enter the artist of the comic:")
        id = 0
        for x in inventory:
            id += 1
        inventory[id] = book(title, genre, releaseDate, author, publisher, artist)
        print("You created a comic")
    elif itemType == "quit":
        print("Stopping process...")
    else:
        print("Error: item type not recognized. Please enter either 'Book' or 'Comic'.")
        createItem()
  
def save():
    json_string = jsonpickle.encode(inventory)
    file = open("inventory.txt", "w")
    file.write(json_string)
    file.close()
    
def load():
    #Inventory is a dictionary containing the item(in the form of a dict) and it's ID number given
    #to it when it entered the system
    #The inventory uses JSON formated text to store the items, the code below opens the 
    inventoryFile = open("inventory.txt", "a") #creates inventory.txt if it is not already there
    inventoryFile.close()
    inventoryFile = open("inventory.txt") #reopens the file to read it
    inventoryRaw = inventoryFile.read() #inventoryRaw stores the raw string that the txt file holds
    inventoryFile.close()
    if not (len(inventoryRaw) == 0): #checks if the file is empty, like if it was just created
        print("Inventory loading...")
        inventory = json.loads(inventoryRaw) # loads the inventory
        # A the moment this load is extremely simple and isn't truely readable yet.
        # ----------Insert load loop here----------
        tempInventory = {}
        book = {"title": "tempVal", 
                "genre": "tempVal", 
                "releaseDate": "tempVal", 
                "author": "tempVal",
                "publisher": "tempVal"}
        comic = {"title": "tempVal", 
                "genre": "tempVal", 
                "releaseDate": "tempVal", 
                "author": "tempVal",
                "publisher": "tempVal",
                "artist": "tempVal"}
        for x in inventory:
            #checks for type of item
            print(x)
            print(inventory[x])
            if inventory[x]['py/object'] == "__main__.book": 
                print("It's a book!")
                tempTitle, tempGenre, releaseDate, author, publisher = "", "", "", "", ""
                #this loop pulls all of the values of the item out of the raw inventory and stores them in temporary variables
                for y in inventory[x]: 
                    if inventory[x] == "py/object":
                        continue
                    elif inventory[x] == "title":
                        tempTitle = inventory[x][y]
                        continue
                    elif inventory[x] == "genre":
                        tempGenre = inventory[x][y]
                        continue
                    elif inventory[x] == "releaseDate":
                        releaseDate = inventory[x][y]
                        continue
                    elif inventory[x] == "author":
                        author = inventory[x][y]
                        continue
                    elif inventory[x] == "publisher":
                        publisher = inventory[x][y]
                tempInventory[int(x)] = inventory[x]
            elif inventory[x]['py/object'] == "__main__.comic":
                print("It's a comic!")
            #assign each value to a tempvariable for use in item init
        inventory = tempInventory
        print("Inventory Loaded.")
        print(inventory)
    else:
        print("No inventory detected")
        print("Initializing inventory")
        inventory = {} #initializes the inventory

#id1 = book("The Hobbit", "High Fantasy", (datetime.datetime(1937, 9, 21)).strftime("%x"), "J. R. R. Tolkien", "George Allen & Unwin")

#inventory[1] = jsonpickle.encode(id1)
#inventoryFile = open("inventory.txt", "w")
#inventoryFile.write(json.dumps(inventory))
#inventoryFile.close()
