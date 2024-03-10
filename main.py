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

def save():
    json_string = jsonpickle.encode(inventory)
    file = open("inventory.txt", "w")
    file.write(json_string)
    file.close()

def createItemSafe():
    #checks if variables within createItem are not going to break the strftime
    day = itemDayTextBox.get()
    month = itemMonthTextBox.get()
    year = itemYearTextBox.get()
    if not (day.isnumeric()):
        itemDayTextBox.insert(0, 'This field must be numeric, from 1-31')
    if not (month.isnumeric()):
        itemMonthTextBox.insert(0, 'This field must be numeric, from 1-12')
    if not (year.isnumeric()):
        itemYearTextBox.insert(0, 'This field must be numeric)
    createItem()

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
            print("ID: ", id)
        inventory[id] = book(title, genre, releaseDate, author, publisher)
        print("You created a book")
        print(id)
        save()
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
            print("ID: ", id)
        inventory[id] = comic(title, genre, releaseDate, author, publisher, artist)
        print("You created a comic")
        print(id)
        save()
    elif itemType == "quit":
        print("Stopping process...")
    else:
        print("Error: item type not recognized. Please enter either 'Book' or 'Comic'.")
        createItem()
    
def load():
    #Inventory is a dictionary containing the item(in the form of a dict) and it's ID number given
    #to it when it entered the system
    #The inventory uses JSON formated text to store the items, the code below 'loads' the inventory from the file of the same name
    inventoryFile = open("inventory.txt", "a") #creates inventory.txt if it is not already there
    inventoryFile.close()
    inventoryFile = open("inventory.txt") #reopens the file to read it
    inventoryRaw = inventoryFile.read() #inventoryRaw stores the raw string that the txt file holds
    inventoryFile.close()
    if not (len(inventoryRaw) == 0): #checks if the file is empty, like if it was just created
        print("Inventory loading...") #Status message for console while testing
        inventory = json.loads(inventoryRaw) # loads the raw inventory. At this moment the inventory is a dictionary of dictionaries, we need it to be a dictionary of items(as per our item class)
        tempInventory = {} # the loop will use this dictionary to store the actual item objects while the function iterates through the list
        for x in inventory: #This loop converts the dictionaries within Inventory into objects and places them in tempInventory
            #First we check what type of item we are looking at
            if inventory[x]['py/object'] == "__main__.book": 
                print("It's a book!") 
                tempTitle, tempGenre, tempReleaseDate, tempAuthor, tempPublisher = "", "", "", "", "" #Initialize attributes of a book
                #this loop pulls all of the values of the item out of the raw inventory and stores them in temporary variables
                for y in inventory[x]: #This loop assigns all of the values of the dictionary we are looking at to the temp attributes above
                    if y == "py/object":
                        continue
                    elif y == "title":
                        print(inventory[x]["title"])
                        tempTitle = inventory[x][y]
                        continue
                    elif y == "genre":
                        tempGenre = inventory[x][y]
                        continue
                    elif y == "releaseDate":
                        tempReleaseDate = inventory[x][y]
                        continue
                    elif y == "author":
                        tempAuthor = inventory[x][y]
                        continue
                    elif y == "publisher":
                        tempPublisher = inventory[x][y]
                    elif y == "artist":
                        tempArtist = inventory[x][y]
                    else:
                        print("Error loading item")
                tempBook = book(tempTitle, tempGenre, tempReleaseDate, tempAuthor, tempPublisher)
                tempInventory[int(x)] = tempBook #assign the item to its respective spot in tempInventory
            elif inventory[x]['py/object'] == "__main__.comic":
                print("It's a comic!")
                tempTitle, tempGenre, tempReleaseDate, tempAuthor, tempPublisher, tempArtist = "", "", "", "", "", "" #Initialize attributes of a book
                #this loop pulls all of the values of the item out of the raw inventory and stores them in temporary variables
                for y in inventory[x]: #This loop assigns all of the values of the dictionary we are looking at to the temp attributes above
                    if y == "py/object":
                        continue
                    elif y == "title":
                        print(inventory[x]["title"])
                        tempTitle = inventory[x][y]
                        continue
                    elif y == "genre":
                        tempGenre = inventory[x][y]
                        continue
                    elif y == "releaseDate":
                        tempReleaseDate = inventory[x][y]
                        continue
                    elif y == "author":
                        tempAuthor = inventory[x][y]
                        continue
                    elif y == "publisher":
                        tempPublisher = inventory[x][y]
                    elif y == "artist":
                        tempArtist = inventory[x][y]
                    else:
                        print("Error loading item")
                tempComic = comic(tempTitle, tempGenre, tempReleaseDate, tempAuthor, tempPublisher, tempArtist)
                tempInventory[int(x)] = tempComic #assign the item to its respective spot in tempInventory
            #assign each value to a tempvariable for use in item init
        inventory = {} #Clears inventory of json string data
        for x in tempInventory:
            inventory[x] = tempInventory[x]
        print("Inventory Loaded.")
        return inventory
    else:
        print("No inventory detected")
        print("Initializing inventory")
        inventory = {} #initializes the inventory
        print("Fresh Inventory initialized")
        return inventory

def display(): #returns a list of every item within inventory
    display = []
    for x in inventory:
        display.append(inventory[x].__str__())
    return display

def filteredDisplay(filteredInventory): #this version of display takes a dictionary instead of defaulting to inventory
    display = []
    for x in filteredInventory:
        display.append(filteredInventory[x].__str__())
    return display
    
def search(filterInput):
    for x in inventory:
        if filterInput in inventory[x].__str__():
            #add item to filtered list
            filteredInven[x] = inventory[x].__str__()
    return filteredInven
#id1 = book("The Hobbit", "High Fantasy", (datetime.datetime(1937, 9, 21)).strftime("%x"), "J. R. R. Tolkien", "George Allen & Unwin")

#inventory[1] = jsonpickle.encode(id1)
#inventoryFile = open("inventory.txt", "w")
#inventoryFile.write(json.dumps(inventory))
#inventoryFile.close()


### Run this as test ###
def main():
    inventory = {}
    inventory = load()
    print(inventory)
    createItem()
    choice = input("Would you like to save? (y/n) ")
    if choice == "y":
        save()
    else:
        print("No changes made")
    print(inventory)

# if __name__ == '__main__':
#     main()
