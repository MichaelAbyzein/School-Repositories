
with open('dat_1.txt', 'r') as file:
    print(type(file))
    lyric = file.read()

print(type(lyric))
print(lyric)

da_lyric = lyric.split("\n")
print(da_lyric)
