a = 0
b = 1
count = 0
max_count = 20

while count < max_count:
    count += 1
    print(a, end=" ")

    anc_a = a
    a = b
    b = anc_a + b
print()