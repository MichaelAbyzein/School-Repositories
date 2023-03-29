"""
sts = [
    ["*", "*", "O", "*", "*"],
    ["*", "O", "*", "O", "*"],
    ["*", "O", "*", "O", "*"],
    ["*", "*", "O", "*", "*"],
    ["*", "O", "*", "O", "*"]
]

for row in sts:
    for st in row:
        print(st, end=" ")
    print()
"""

sts = []

rows = 10
cols = 10

for ro in range(rows):
    l = []
    for cl in range(cols):
        print("*", end=" ")
        l.append("*")
    sts.append(l)
    print() # "\n"
    
print()

for row in sts:
    for st in row:
        print(st, end=" ")
    print()