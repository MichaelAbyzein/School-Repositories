import json
from random import randint

def load_dat():
    with open("dat.json", "r") as file:
        return json.load(file)

def save(t):
    with open("dat.json", "w") as file:
        json.dump(t, file)
        return True

def get_stored_num():
    try:
        return load_dat()
    except:
        return
    
def get_new_fav_num(rnum):
    resp = input(f"Is your favorite number {rnum} (y/n) ")
    if resp.lower() == "y":
        return rnum
    elif resp.lower() == "n":
        return input("So, what is it? ")
    else:
        print("Please, answer with y or n.")
        return get_new_fav_num(rnum)

def ask_us():
    fav_num = get_stored_num()
    if fav_num:   
        print(f"I know your favorite number, it's {fav_num}")
    else:
        guess = randint(0, 400)
        fav_num = get_new_fav_num(guess)
        save(fav_num)
        print(f"I'll remember that")
      
ask_us()
