#Try Except.... "Handling Error"

while True:
    a = input("a = ")
    b = input("b = ")
    
    try:
        print(f"a : b = {int(a)/int(b)}")
    except:
        print(f"Invalid Division by 0")

    quit = input("Quit (y/n)? ")
    if quit == "y":
        break