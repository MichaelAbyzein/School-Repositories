from random import randint
import os
def clscr():
    os.system("cls")

tries = 1
tmax = 5

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
    ui = input("Enter Ship Location: ").split(" ")
    if dy_vessel == ui:
        return True
    else:
        dy_board[int(ui[0])][int(ui[1])] = "X"
        return False

run = True
vic = False
defe = False

dy_board = set_board(5)
dy_vessel = set_ves_loc(5)

while run == True:
    print_board(dy_board)
    print(dy_vessel)
    if  tries < 6:
        print(f"You have tried {tries} time(s) (max = {tmax})")
    defe = ck_tr()
    if vic == False and defe == False:
        vic = ck_ui()
    if not vic:
        tries += 1
    if defe == True:
        print("GAME OVER")
        cond = input("Do you want to retry? (Y/N): ")
        if cond == "Y":
            clscr()
            tries = 1
            vic = False
        if cond == "N":
            run = False
    if vic == True: 
        print(f"Congrats, That's a hit, with {tries} tries.")
        conv = input("Do you want to continue? (Y/N): ")
        if conv == "Y":
            clscr()
            tries = 1
            vic = False
        if conv == "N":
            run = False