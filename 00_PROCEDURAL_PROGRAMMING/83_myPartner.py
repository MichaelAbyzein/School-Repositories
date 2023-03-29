name = input()
my_num = 0

for char in name.upper():
    my_num += ord(char)
    
print(f"Inisial Jodoh Kamu adalah {chr(my_num%26+ord('A'))}")