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
from models import *



#####-------------Bo's Work-------------#####
        


        
def main():
    # inventory = load_inventory()
    # while True:
    #     print("\nInventory Management System")
    #     choice = input("1. Add Item\n2. Update Item \n3. Remove Item\n4. Save and Exit \n5. Print Inventory \n6. View Item Details \nEnter your choice: ")
    #     if choice == '1':
    #         add_item(inventory)
    #     elif choice == '2':
    #         update_item(inventory)
    #     elif choice == '3':
    #         remove_item(inventory)
    #     elif choice == '4':
    #         save_inventory(inventory)
    #         print("Inventory saved. Exiting program.")
    #         break
    #     elif choice == '5':
    #         print_inventory(inventory)
    #     elif choice == '6':
    #         view_item_details(inventory)
    #     else:
    #         print("Invalid choice.")

    inventory = inventoryApp()
    inventory.mainloop()


if __name__ == '__main__':
    main()



    
########-----------Bo's Work end-----------########
