import json

with open('dat.json', 'r') as file:
    owners = json.load(file)
    
#print(owners)
for owner, pets in owners.items():
    print(f"-{owner.title()}:")
    for pet in pets:
        print(f"\t* {pet.title()}")
    print()