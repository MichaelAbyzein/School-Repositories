# regular arg with arbitrary arguments

def make_pizza(size, *toppings):
    print(f"\n Making a {size}cm pizza with the following topping:")
    #print(toppings)
    #False : list kosong, string kosong, None, 0, dict kosong
    
    if toppings: # len(toppings) > 0
        for topping in toppings:
            print(f"\t-{topping}")
    
    else:
        print("No topping.")
    
make_pizza(32)
make_pizza(15, "banana")
make_pizza(22, "banana", "pineapple", "cheese")