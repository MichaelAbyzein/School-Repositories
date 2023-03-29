"""

rows = 5

* * * * *
* * * *
* * *
* *
*

"""

rows = 20

for row in range(rows):
    for star in range(rows-row):
        print("*", end=" ")
    print()