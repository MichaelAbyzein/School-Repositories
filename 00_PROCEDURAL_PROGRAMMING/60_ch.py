"""

rows = 5
    *
   **
  ***
 ****
*****

"""

rws = 5

for rw in range(rws):
    for spa in range(rws-rw):
        print(" ", end=" ")
    for sta in range(rw+1):
        print("*", end=" ")
    print()