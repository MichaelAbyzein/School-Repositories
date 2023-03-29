"""
factorial
4! = 4 x 3 x 2 x 1 = 24
3! = 3 x 2 x 1 = 6
5! = 5 x 4 ... x 1
100! = 100 x 99 x ... x 1
0! = ?
-m! = ?
m/n! = m dan n bukan 0

"""

def factor(dat):
    if dat < 0 or dat > 998:
        return "NOT DEFINED"
    if dat == float(dat):
        return "NOT INTEGER, REEEEEEEEEEEEEEE!"
    if dat == 1 or dat == 0:
        return 1
    return dat * factor(dat-1)

print(factor(1/5))