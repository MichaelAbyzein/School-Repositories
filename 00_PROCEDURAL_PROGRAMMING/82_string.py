string = "HELP"

list_chars = ["H", "E", "L", "P"]

print(len(string))
print(len(list_chars))

for char in string:
    print(char, end=" ")
print()

for char in list_chars:
    print(char, end=" ")
print()

#slicing lists and string
print(string[0], list_chars[0])
print(string[0:2], list_chars[0:2])
print(string[0:3:2], list_chars[0:3:2])