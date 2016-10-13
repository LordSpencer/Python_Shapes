from Myro import *
init("sim")
penDown()

def Polygon():
    sides=input("Number of sides?")
    sides = int(sides)
    i = sides
    while i>0:
        turnBy(360/sides)
        forward(sides,1)
        i = i-1
Polygon()