error = False

while not error:
    print("We are playinng now!")
    still_playing = input("Still playing (Y/N) : ")
    if still_playing == "N":
        print("Thanks for playing!")
        error = True