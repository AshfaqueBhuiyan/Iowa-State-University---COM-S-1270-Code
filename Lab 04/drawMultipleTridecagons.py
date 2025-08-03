# Ash Bhuiyan                                                 07-02-2025
# Lab 4 - Drawing of multiple tridecagons in a row using turtle graphics

import turtle

def tridecagonTurtle(s, x, y, t):
    t.penup()
    t.goto(x, y)
    t.pendown()
    angle = 360 / 13
    for i in range(13):
        t.forward(s)
        t.left(angle)

def drawMultipleTridecagons(s, x, y, nr, sr, t):
    for i in range(nr):
        a = x + i * sr
        tridecagonTurtle(s, a, y, t)

def main():
    s = int(input("Enter side length: "))
    x = int(input("Enter starting x-coordinate: "))
    y = int(input("Enter y-coordinate: "))
    nr = int(input("How many tridecagons to draw?: "))
    sr = int(input("Spacing between shapes (x-axis): "))

    screen = turtle.Screen()
    t = turtle.Turtle()
    drawMultipleTridecagons(s, x, y, nr, sr, t)
    turtle.done()

if __name__ == "__main__":
    main()
