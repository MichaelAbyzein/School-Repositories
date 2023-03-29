import os
import getpass

correct_username = "RungusBungus"
correct_pass = "IWantToSayTheNWord"

auth = False
os.system("cls")
while not auth:
    username = input("Insert username : ")
    password = getpass.getpass("Insert password : ")
    
    if username == correct_username and password == correct_pass:
        print(f"Welcome, {username}")
        auth = True
    else:
        print("Username or password doesn't match, please try again")