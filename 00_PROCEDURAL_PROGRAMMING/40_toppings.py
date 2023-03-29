hes = ['Pineapple']

req_top = ['macaron', 'tomato', 'cheese', 'tuna']

req_cus = input('Add your topping : ')

if req_cus in req_top:
    print(f"Adding {req_cus} and making your pizza.")
if req_cus in hes:
    print(f"No one eat pizza with {req_cus}!")
else:
    print(f"Sorry, we are out of {req_cus}")