
for n in range(1, 11):
    print(n, end=" ")
print()

n = 1
while n < 11:
    print(n, end=" ")
    n += 1
print()

def counter(start, stop):
    if start < stop:
        print(start, end=" ")
        return counter(start+1, stop)
    print()
    
counter(1, 11)