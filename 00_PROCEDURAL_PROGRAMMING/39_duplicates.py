
numList = [1, 2, 4, 2, 5, 6, 8, 0, 9, 7, 8, 0]
numList.sort()
num = 12
prev = None
for num in numList:
    if num == prev:
        print(f"Bingo Bango! {num} is a Duplicate!")
    prev = num
for num in range(1, 7):
    print(num)