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
import tkinter as tk
import models
from models import book, comic, boardGame
from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk


#Other GUI variables
TXT_HEIGHT = 1
TXT_WIDTH = 37
VERT_PAD = 10
BORDER = 5
BUTTON_SPACE = 5
SORTING = ""
TYPE_LIST = ["Book", "Comic", "Board Game"]

inventory = {}

def save():
    json_string = jsonpickle.encode(inventory)
    file = open("inventory.txt", "w")
    file.write(json_string)
    file.close()

def createItem(): 
    date_format = '%Y-%m-\%d'
    itemType = itemTypeComboBox.get()
    print("item type")
    if itemType == "Book":
        title = itemTitleTextBox.get()
        genre = itemGenreTextBox.get()
        year = itemYearTextBox.get()
        month = itemMonthTextBox.get()
        day = itemDayTextBox.get()
        releaseDate = (datetime(int(year), int(month), int(day))).strftime("%x")
        author = itemAuthorTextBox.get()
        publisher = itemPublisherTextBox.get()
        id = 0
        for x in inventory:
            id += 1
            print("ID: ", id)
        inventory[id] = book(title, genre, releaseDate, author, publisher)
        print("You created a book")
        print(id)
        save()
    elif itemType == "Comic":
        title = itemTitleTextBox.get()
        genre = itemGenreTextBox.get()
        year = itemYearTextBox.get()
        month = itemMonthTextBox.get()
        day = itemDayTextBox.get()
        releaseDate = (datetime(int(year), int(month), int(day))).strftime("%x")
        author = itemAuthorTextBox.get()
        publisher = itemPublisherTextBox.get()
        artist = itemArtistTextBox.get()
        id = 0
        for x in inventory:
            id += 1
            print("ID: ", id)
        inventory[id] = comic(title, genre, releaseDate, author, publisher, artist)
        print("You created a comic")
        print(id)
        save()
    elif itemType.lower() == "board game":
        title = itemTitleTextBox.get()
        genre = itemGenreTextBox.get()
        year = itemYearTextBox.get()
        month = itemMonthTextBox.get()
        day = itemDayTextBox.get()
        releaseDate = (datetime(int(year), int(month), int(day))).strftime("%x")
        designer = itemDesignerTextBox.get()
        publisher = itemPublisherTextBox.get()
        artist = itemArtistTextBox.get()
        numPlayers = itemPlayersTextBox.get()
        gameFormat = itemFormatTextBox.get()
        playingTime = itemTimeTextBox.get()
        id = 0
        for x in inventory:
            id += 1
            print("ID: ", id)
        inventory[id] = boardGame(title, genre, releaseDate, numPlayers, playingTime, publisher, gameFormat, designer, artist)
        print("You created a board game")
        print(id)
        save()
    elif itemType == "quit":
        print("Stopping process...")
    else:
        print("Error: item type not recognized. Please enter either 'Book' or 'Comic'.")
        createItem()
    show()
    
def load():
    #Inventory is a dictionary containing the item(in the form of a dict) and it's ID number given
    #to it when it entered the system
    #The inventory uses JSON formated text to store the items, the code below 'loads' the inventory from the file of the same name
    inventoryFile = open("inventory.txt", "a") #creates inventory.txt if it is not already there
    inventoryFile.close()
    inventoryFile = open("inventory.txt", "r") #reopens the file to read it
    inventoryRaw = inventoryFile.read() #inventoryRaw stores the raw string that the txt file holds
    inventoryFile.close()
    if not (len(inventoryRaw) == 0): #checks if the file is empty, like if it was just created
        print("Inventory loading...") #Status message for console while testing
        inventory = json.loads(inventoryRaw) # loads the raw inventory. At this moment the inventory is a dictionary of dictionaries, we need it to be a dictionary of items(as per our item class)
        tempInventory = {} # the loop will use this dictionary to store the actual item objects while the function iterates through the list
        for x in inventory: #This loop converts the dictionaries within Inventory into objects and places them in tempInventory
            #First we check what type of item we are looking at
            if inventory[x]['py/object'] == "models.book": 
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
            elif inventory[x]['py/object'] == "models.comic":
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
            elif inventory[x]['py/object'] == "models.boardGame":
                print("It's a board game!")
                tempTitle, tempGenre, tempReleaseDate, tempNumPlayers, tempPlayingTime, tempPublisher, tempGameFormat, tempDesigner, tempArtist = "", "", "", "", "", "", "", "", "" #Initialize attributes of a book
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
                    elif y == "tempNumPlayers":
                        tempAuthor = inventory[x][y]
                        continue
                    elif y == "tempPlayingTime":
                        tempAuthor = inventory[x][y]
                        continue
                    elif y == "tempPublisher":
                        tempAuthor = inventory[x][y]
                        continue
                    elif y == "tempGameFormat":
                        tempAuthor = inventory[x][y]
                        continue
                    elif y == "tempDesigner":
                        tempAuthor = inventory[x][y]
                        continue
                    elif y == "artist":
                        tempArtist = inventory[x][y]
                    else:
                        print("Error loading item")
                tempBoardGame = boardGame(tempTitle, tempGenre, tempReleaseDate, tempNumPlayers, tempPlayingTime, tempPublisher, tempGameFormat, tempDesigner, tempArtist)
                tempInventory[int(x)] = tempBoardGame #assign the item to its respective spot in tempInventory
            #assign each value to a tempvariable for use in item init
        print(tempInventory)
        inventory = {} #Clears inventory of json string data
        for x in tempInventory:
            inventory[x] = tempInventory[x]
        print("Inventory Loaded.")
        print(inventory.keys())
        return inventory
    else:
        print("No inventory detected")
        print("Initializing inventory")
        inventory = {} #initializes the inventory
        print("Fresh Inventory initialized")
        return inventory
    

def delete():
    global inventory
    tempInventory = inventory
    inventory = {}
    count = 0
    for x in tempInventory:
        inventory[count] = tempInventory[x]
    obj = inventoryViewBox.curselection()
    print(obj)
    for x in obj:
        inventory.pop(int(x))
    save()
    show()
    


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
        itemYearTextBox.insert(0, 'This field must be numeric')
    createItem()

#returns a list of every item within inventory
def display():
    display = []
    for x in inventory:
        display.append(inventory[x].__str__())
    return display

def show():   
    #Add data to listbox
    content = display()
    inventoryViewBox.delete(0,END)
    count = 0
    for x in content:
        inventoryViewBox.insert(count, x)
        count += 1

if __name__ == '__main__':
    

    #Main GUI variable
    gui = tk.Tk()
    gui.title("Library Manager")


    
    
    #Item type variable
    itemType = ""

    #Book related variables
    title       = []
    genre       = []
    year        = []
    month       = []
    day         = []
    releaseDate = []
    author      = []
    publisher   = []
    id          = []
    artist      = []



    #GUI objects
    topPane                = tk.PanedWindow(gui)
    itemTypeComboBox       = ttk.Combobox(gui, width=48, values=["Book", "Comic", "Board Game"])
    itemTitleLabel         = tk.Label(gui, text="Title: ")
    itemTitleTextBox       = tk.Entry(gui, width=TXT_WIDTH, bd=BORDER)
    itemGenreLabel         = tk.Label(gui, text="Genre: ")
    itemGenreTextBox       = tk.Entry(gui, width=TXT_WIDTH, bd=BORDER)
    itemYearLabel          = tk.Label(gui, text="Year: ")
    itemYearTextBox        = tk.Entry(gui, width=TXT_WIDTH, bd=BORDER)
    itemMonthLabel         = tk.Label(gui, text="Month: ")
    itemMonthTextBox       = tk.Entry(gui, width=TXT_WIDTH, bd=BORDER)
    itemDayLabel           = tk.Label(gui, text="Day: ")
    itemDayTextBox         = tk.Entry(gui, width=TXT_WIDTH, bd=BORDER)
    itemAuthorLabel        = tk.Label(gui, text="Author: ")
    itemAuthorTextBox      = tk.Entry(gui, width=TXT_WIDTH, bd=BORDER)
    itemPublisherLabel     = tk.Label(gui, text="Publisher: ")
    itemPublisherTextBox   = tk.Entry(gui, width=TXT_WIDTH, bd=BORDER)
    itemIdLabel            = tk.Label(gui, text="ID: ")
    itemIdTextBox          = tk.Entry(gui, width=TXT_WIDTH, bd=BORDER)
    itemArtistLabel        = tk.Label(gui, text="Artist: ")
    itemArtistTextBox      = tk.Entry(gui, width=TXT_WIDTH, bd=BORDER)
    itemDesignerLabel      = tk.Label(gui, text="Designer: ")
    itemDesignerTextBox    = tk.Entry(gui, width=TXT_WIDTH, bd=BORDER)
    itemPlayersLabel       = tk.Label(gui, text="# of players:")
    itemPlayersTextBox     = tk.Entry(gui, width=TXT_WIDTH, bd=BORDER)
    itemFormatLabel        = tk.Label(gui, text="Format: ")
    itemFormatTextBox      = tk.Entry(gui, width=TXT_WIDTH, bd=BORDER)
    itemTimeLabel          = tk.Label(gui, text="Play Time: ")
    itemTimeTextBox        = tk.Entry(gui, width=TXT_WIDTH, bd=BORDER)
    addSelectButton        = tk.Button(gui, height = 1, width = 10, text = "Add to library", command = createItemSafe)
    deleteEntryButton      = tk.Button(gui, height = 1, width = 10, text = "Delete entry", command = delete)
    inventoryViewBox       = tk.Listbox(gui, height = 20, width = 200, bd = BORDER)

    #Inventory variables and load
    inventory = {}
    filteredInven = {}
    inventory = load()
    show()

    #Add objects to appropriate pane

    topPane.add(itemTitleLabel)
    topPane.add(itemTitleTextBox)
    topPane.add(itemGenreLabel)
    topPane.add(itemGenreTextBox)
    topPane.add(itemYearLabel)
    topPane.add(itemYearTextBox)
    topPane.add(itemMonthLabel)
    topPane.add(itemMonthTextBox)
    topPane.add(itemDayLabel)
    topPane.add(itemDayTextBox)
    topPane.add(itemAuthorLabel)
    topPane.add(itemAuthorTextBox)
    topPane.add(itemPublisherLabel)
    topPane.add(itemPublisherTextBox)
    topPane.add(itemIdLabel)
    topPane.add(itemIdTextBox)
    topPane.add(itemArtistLabel)
    topPane.add(itemArtistTextBox)
    topPane.add(addSelectButton)
    topPane.add(deleteEntryButton)
    topPane.add(inventoryViewBox)
    topPane.add(itemTypeComboBox)
    topPane.add(itemDesignerLabel)
    topPane.add(itemDesignerTextBox)
    topPane.add(itemPlayersLabel)
    topPane.add(itemPlayersTextBox)
    topPane.add(itemFormatLabel)
    topPane.add(itemFormatTextBox)
    topPane.add(itemTimeLabel)
    topPane.add(itemTimeTextBox)

    
    #Position objects using .grid method
    itemTitleLabel        .grid(column = 0, row = 1, pady = VERT_PAD)
    itemGenreLabel        .grid(column = 0, row = 2, pady = VERT_PAD)
    itemYearLabel         .grid(column = 0, row = 3, pady = VERT_PAD)
    itemMonthLabel        .grid(column = 0, row = 4, pady = VERT_PAD)
    itemDayLabel          .grid(column = 0, row = 5, pady = VERT_PAD)
    itemAuthorLabel       .grid(column = 0, row = 7, pady = VERT_PAD)
    itemPublisherLabel    .grid(column = 0, row = 8, pady = VERT_PAD)
    itemIdLabel           .grid(column = 0, row = 9, pady = VERT_PAD)
    itemArtistLabel       .grid(column = 0, row = 10, pady = VERT_PAD)
    itemTitleTextBox      .grid(column = 1, row = 1, pady = VERT_PAD)
    itemGenreTextBox      .grid(column = 1, row = 2, pady = VERT_PAD)
    itemYearTextBox       .grid(column = 1, row = 3, pady = VERT_PAD)
    itemMonthTextBox      .grid(column = 1, row = 4, pady = VERT_PAD)
    itemDayTextBox        .grid(column = 1, row = 5, pady = VERT_PAD)
    itemAuthorTextBox     .grid(column = 1, row = 7, pady = VERT_PAD)
    itemPublisherTextBox  .grid(column = 1, row = 8, pady = VERT_PAD)
    itemIdTextBox         .grid(column = 1, row = 9, pady = VERT_PAD)
    itemArtistTextBox     .grid(column = 1, row = 10, pady = VERT_PAD)
    addSelectButton       .grid(column = 3, row = 11, pady = VERT_PAD)
    deleteEntryButton     .grid(column = 3, row = 12, pady = VERT_PAD)
    itemTypeComboBox      .grid(column = 0, row = 0, pady = VERT_PAD)
    inventoryViewBox      .grid(column = 2, row = 1, pady = VERT_PAD)
    itemDesignerLabel     .grid(column = 0, row = 11, pady = VERT_PAD)
    itemDesignerTextBox   .grid(column = 1, row = 11, pady = VERT_PAD)
    itemPlayersLabel      .grid(column = 0, row = 12, pady = VERT_PAD)
    itemPlayersTextBox    .grid(column = 1, row = 12, pady = VERT_PAD)
    itemFormatLabel       .grid(column = 0, row = 13, pady = VERT_PAD)
    itemFormatTextBox     .grid(column = 1, row = 13, pady = VERT_PAD)



    #Display GUI
    gui.mainloop()
