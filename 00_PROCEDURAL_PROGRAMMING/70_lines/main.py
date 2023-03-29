
with open('dat_1.txt', 'r') as file:
    lyric = file.readlines()

print(lyric)
cl_lyric = []
for lyrics in lyric:
    cl_lyric.append(lyrics.strip())
print(cl_lyric)