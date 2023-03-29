# Angka harus kelipatan 3

num = float(input("Give me a number: "))
if num % 3 == 0:
    print(f"{num} is a multiples of three")
else:
    print(f"{num} is not a multiples of three")