import turtle
import os
from random import randint

a = turtle.Pen()
a.shape("turtle")
a.down()
a.speed("fastest")
a.color("red")
b = turtle.Pen()
b.shape("turtle")
b.down()
b.speed("fastest")
b.color("blue")

run = True
run1 = True
run2 = True
c1 = True
c2 = True
while run == True:
    while run1 == True:
        if c1 == True:
            ang1 = randint(-360, 360)
            msp1 = randint(-10, 10)
            c1 = False

        if c1 == False:
            ang1 = randint(-360, 360)
            msp1 = randint(-10, 10)
            c1 = True
            
        if run1 == True:
            c1 = False
            a.left(ang1)
            c1 = True
            a.forward(msp1)
            c1 = False
            a.right(ang1*-1)
            c1 = True
            a.backward(msp1*-1)
            c1 = False
            a.right(ang1)
            c1 = True
            a.forward(msp1)
            c1 = False
            a.left(ang1*-1)
            c1 = True
            a.backward(msp1*-1)
            os.system("cls")
            print(f"A's Step: {msp1}")
            print(f"A's Angle: {ang1}")
            run2 = True
            run1 = False
            
    while run2 == True:

        if c2 == True:
            ang2 = randint(-360, 360)
            msp2 = randint(-10, 10)
            c2 = False

        if c2 == False:
            ang2 = randint(-360, 360)
            msp2 = randint(-10, 10)
            c2 = True
            
        if run2 == True:
            c2 = False
            b.left(ang2)
            c2 = True
            b.forward(msp2)
            c2 = False
            b.right(ang2*-1)
            c2 = True
            b.backward(msp2*-1)
            c2 = False
            b.right(ang2)
            c2 = True
            b.forward(msp2)
            c2 = False
            b.left(ang2*-1)
            c2 = True
            a.backward(msp2*-1)
            os.system("cls")
            print(f"B's Step: {msp2}")
            print(f"B's Angle: {ang2}")
            run1 = True
            run2 = False