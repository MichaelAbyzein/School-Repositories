# al = [1, 2, 3, 4, 5]
al = [
    [1, 2, 3, 4, 5], # [0][0] [0][1] [0][2]
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20]
]

"""
for item in al:
    print(item, end=" ")
print()
"""

for row in al:
    for cl in row:
        print(cl, end=" ")
    print()
