from random import randint
import json
import os
def clscr():
    os.system("cls")

tries = 1
tmax = 6

def intro():
    try:
        os.system("cls")
        print("Welcome to Battleship CMD Edition")
        res = int(input("Please input how many rows you wanna play: "))
        
        if res < 3 or res > 20:
            print("You must input a number between 3 or 20!")
            input("Enter to try again")
            return intro()
            
        return res
    except ValueError as e:
        print("You must enter an integer number!")
        input("Enter to try again")
        return intro()
    
    return input("Please input how many rows you wanna play: ")

def set_board(rows):
    board = []
    
    for row in range(rows):
        ln = []
        for item in range(rows):
            ln.append("0")
        board.append(ln)
    return board

def set_ves_loc(rows):
    loc = [str(randint(0, rows-1)), str(randint(0, rows-1))] # [x, y]
    return loc
    
def print_board(board):
    clscr()
    for row in board:
        for item in row:
            print(item, end =" ")
        print()

def ck_tr():
    if tries == tmax:
        return True
    else:
        return False
        
def ck_ui():
    try:
        ui = input("Enter Ship Location: ").split(" ")
        if len(ui) != 2:
            print("You must input 2 integer number!")
            input("Enter to Try Again")
            return ck_ui()
        ui = [str(int(ui[0])-1), str(int(ui[1])-1)]
    except ValeError as crsh:
        print("You must input an integer number!")
        input("Enter to Try Again")
        return ck_ui()
    else:
        if int(ui[0]) < 0 or int(ui[0]) > rows-1 or int(ui[1]) < 0 or int(ui[1]) > rows-1:
            print(f"You must input number between 1 and {rows}")
            input("Enter to Try Again")
            return ck_ui()
        if dy_vessel == ui:
            return True
        dy_board[int(ui[0])][int(ui[1])] = "X"
        return False

run = True
vic = False
defe = False
rows = intro()

dy_board = set_board(rows)
dy_vessel = set_ves_loc(rows)

while run == True:
    print_board(dy_board)
    if  tries < tmax + 1:
        print(f"You have tried {tries} time(s) (max = {tmax})")
    defe = ck_tr()
    vic = ck_ui()
    if not vic:
        tries += 1
    if defe == True:
        clscr()
        print("GAME OVER")
        cond = input("Do you want to retry? (Y/N): ")
        if cond == "Y":
            clscr()
            tries = 1
            vic = False
        if cond == "N":
            clscr()
            run = False
    if vic == True: 
        clscr()
        print(f"Congrats, That's a hit, with {tries} tries.")
        run = False