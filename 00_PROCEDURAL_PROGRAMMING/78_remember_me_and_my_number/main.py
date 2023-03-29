import json
from random import randint

def load_data():
    try:
        with open("dat.json", "r") as file:
            return json.load(file)
    except:
        return {} # {} != None

def save(data):
    with open("dat.json", "w") as file:
        json.dump(data, file)
        return True

def hello_user(data):
    #print (f"{hex(id(data))}, {type(data)}")
    name = input("What is your name ? ")
    if name in data:
        print(f"Welcome back {name}")
    else:
        data[name] = None
        save(data)
        print("I'll remember you when you return!")
    return name
        
def get_new_fav_num(rnum):
    resp = input(f"Is your favorite number {rnum} (y/n) ")
    if resp.lower() == "y":
        return rnum
    elif resp.lower() == "n":
        try:
            return int(input("So, what is it ? "))
        #2 handling error kalau bukan integer number yg diinput
    else:
        print("Please, answer with y or n.")
        return get_new_fav_num(rnum)        

def ask_user(data, user):
    if user in data:
        if data[user]:
            print(f"I know your favorite number, it is {data[user]}")
            #1 tawaran mau ubah favorite number
        else:
            guess = randint(0, 400)
            fav_num = get_new_fav_num(guess)
            data[user] = fav_num
            save(data)
            print(f"I'll remember your favorite number!")
    
data_master = load_data()
ask_user(data_master, hello_user(data_master)) #pass ny reference
#print (f"{hex(id(data))}, {type(data)}")