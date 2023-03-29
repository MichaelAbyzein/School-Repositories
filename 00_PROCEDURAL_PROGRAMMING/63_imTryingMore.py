#Try Except.... "Handling Error"
import os
while True:
    os.system("cls")
    a = input("a = ")
    b = input("b = ")
    
    try:
        res = int(a)/int(b)
    except ZeroDivisionError as err:
        print(f"Invalid Division by zero.\nError: {err}")
    except ValueError:
        print("You must input an integer number!")
    else:
        print(f"a : b = {res}")
    finally:
        print("And Done!")

    quit = input("Quit (y/n)? ")
    if quit == "y":
        os.system("cls")
        break

ValueError
ZeroDivisionError

"""
while:
    pass
else:
    pass
for i in range():
    pass
else:
    pass
"""