"""

*
**
***
****

"""

rows = 6
# range -> range(start, stop, step)

for row in range(rows): # range(0, 5, 1)
    for star in range(row):
        print("*", end=" ")
    print()