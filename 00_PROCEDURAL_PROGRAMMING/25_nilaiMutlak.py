a = 23
b = -23

def nilai_mutlak(n):
    if n < 0:
        n = -n
    return n
    
if nilai_mutlak(a) == nilai_mutlak(b):
    print(f"Nilai Mutlak dari {a} dan {b} sama")
else:
    print(f"Nilai Mutlak dari {a} dan {b} berbeda")