import os
os.system("title Wishlist Test")

def clearscr():
    os.system("cls")

def menu_print():
    print("1. Look Wishlist")
    print("2. Add Item to Wishlist")
    print("3. Delete Item from Wishlist")
    print("4. Change Item in Wishlist")
    print("Q. Quit from Wishlist")

def show_wistlist():
    print("Wishlist:")
    #print(wishlist)
    if len(wishlist) > 0:
        index = 0
        while index < len(wishlist):
            print(index,".",wishlist[index])
            index += 1
    else:
        print("There is no item in the wishlist.")
    input("Press ENTER to return to the menu")

def addit():
    print("Add Items")
    new_it = input("Insert item you want to add on the list : ")
    if len(new_it) > 0:
        wishlist.append(new_it)
        print("Item has been added.")
    else:
        print("Item inserted are invalid!")
    input("Press ENTER to return to menu")
    
def delit():
    print("Delete Item")
    del_it = input("Insert Item that want to be removed: ")
    if del_it in wishlist:
        wishlist.remove(del_it)
        print("Item has been removed.")
    else:
        print("Item not Found")
    input("Press ENTER to return to menu.")
    
def changeit():
    print("Change Item")
    chan_it = input("Insert item that you want to change: ")
    if chan_it in wishlist:
        id = wishlist.index(chan_it)
        new_it = input("Insert the new item name: ")
        wishlist[id] = new_it
        print("Item has been changed!")
    else:
        print("Item was not found!")
    input("Press ENTER to return to menu.")
    
wishlist = ["Pen", "Water Bottle"]
choice = None

running = True

while running:

    clearscr()
    menu_print()
    
    choice = input("Insert Menu Choice: ")
    if choice == "1":
        clearscr()
        show_wistlist()
    elif choice == "2":
        clearscr()
        addit()
    elif choice == "3":
        clearscr()
        delit()
    elif choice == "4":
        clearscr()
        changeit()
    elif choice == "Q":
        running = False
 
clearscr()
print("Thank you, bye!")