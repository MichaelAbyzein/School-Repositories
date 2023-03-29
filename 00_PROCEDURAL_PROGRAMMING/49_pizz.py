#Nesting a list in a dictionary

pizza = {
    'crust': 'thick',
    'toppings': ['wurst', 'cheese', 'tomatoes', 'onion']
}

print(pizza['toppings'][2])

for toppings in pizza['toppings']:
    print(f"\t{toppings}")