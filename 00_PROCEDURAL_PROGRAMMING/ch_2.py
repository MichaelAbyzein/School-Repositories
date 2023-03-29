"""
Barisan pangkat 5
"""
a = 1
b = 5
c = 0
mc = 10

while c < mc:
    c += 1
    print(a, end=" ")

    old_a = a
    a = old_a * b
print()