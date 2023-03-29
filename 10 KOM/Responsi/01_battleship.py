from os import system
import random

#def set_board():
#	return ["X" * n for _ in range(n)]

set_board = lambda n : [ list("X" * n) for ඞ in range(n)]

setting_ship = lambda rows : [random.randint(0, rows-1), random.randint(0, rows-1)]

def print_board(board):
	system("cls") # mac : clear
	for row in board:
		print(" ".join(row))

# def setting_ship(rows):
	# location = [random.randint(0, rows-1), random.randint(0, rows-1)]
	# return location

def check_input():
	user_input = list(map(int, input("Enter the coordinate to strike (<x>, <y>): ").split()))

	if user_input == my_ship:
		print("You win!")
		return True
	else:
		attempt =+ 1
	my_board[user_input[0]][user_input[1]] = "0"

	return False

win = False
attempt = 0
rows = 5
my_board = set_board(rows)
my_ship = setting_ship(rows)

while not win:
	print_board(my_board)
	print("Attempt: ", attempt)
	win = check_input()