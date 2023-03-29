import os
username = "admin"
password = "32868"
trying = 0
limit_try = 5

while trying < limit_try:
    ins_user = input("Masukan password: ")
    ins_pass = input("Masukan Username: ")
    if ins_pass == password and ins_user == username:
        os.system("cls")
        print("Welcome back!")
    else:
        os.system("cls")
        trying += 1
        input(f"Wrong password or username, try again! Press ENTER to continue. You only have {trying} tries!")
        os.system("cls")
print("You failed 5 times!")