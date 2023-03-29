

pizzas = {
    "cheeseburger" : {
        "ingridients" : ['bbq minced steak', 'cheddar', 'mustard', 'mozarella'],
        "price" : 340
    },
    "meat lovers" : {
        "ingridients" :['beef sausage', 'minced beef', 'beef burger', 'chicken sausage', 'mozarella'],
        "price" : 630
    }
}

for pizza, info in pizzas.items():
    print(f"\n{pizza.title()}:")
    
    for a_info, data in info.items():
        print(f"\t{a_info}:")
        if type(data) == list:
            for item in data:
                print(f"\t\t- {item}")
        else:
            print(f"\t\t{data}")
                
    print()