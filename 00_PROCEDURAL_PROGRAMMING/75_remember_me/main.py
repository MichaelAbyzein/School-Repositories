import json

filename = "remem.json"
try:
    with open(filename, "r") as file:
        entity = json.load(file)
except:
    entity = input("What are you? ")
    
    with open(filename, "w") as file:
        json.dump(entity, file)
    
    print("I'll remember your name, friend.")
    
else:
    print(f"Hello, {entity}.")