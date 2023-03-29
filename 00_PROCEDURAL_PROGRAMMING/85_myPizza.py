# arbitrary arguments

def make_pizza(*toppings):
    print("\n Making pizza with the following topping:")
    #print(toppings)
    #False : list kosong, string kosong, None, 0, dict kosong
    
    if toppings: # len(toppings) > 0
        for topping in toppings:
            print(f"\t-{topping}")
    
    else:
        print("No topping.")
    
make_pizza()
make_pizza("banana")
make_pizza("banana", "pineapple", "cheese")