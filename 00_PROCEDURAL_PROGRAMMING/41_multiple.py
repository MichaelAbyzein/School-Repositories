
avail_top = ['macaron', 'tomato', 'cheese', 'tuna']

req_tops = []

for_tops = ['pineapple', 'tofu']

end = False

while not end:
    top = input("Input your topping here ('q' to quit): ")
    if top != 'q':
        req_tops.append(top)
    else:
        end = True
        
for req_top in req_tops:
    if req_top in avail_top:
        print(f"Adding {req_top}.")
    if req_top in for_tops:
        print(f"Who eat pizza with {req_top} anyway? Heresy!")
    else:
        print(f"Sorry, we don't have {req_top}.")
        
print("Finished making your pizza...")