# Ash Bhuiyan                                       06-29-2025
# Lab 3 - Drawing a tridecagon using turtle.

# CITATION - URL: https://testbook.com/maths/tridecagon
# CITATION - Author: testbook
# CITATION - Date Accessed: 06-29-2025

import turtle

def tridecagonTurtle(s, x, y, t):
    t.penup()
    t.goto(x, y)
    t.pendown()
    angle = 360 / 13
    for i in range(13):
        t.forward(s)
        t.left(angle)

def main():
    s = int(input("Enter side length (s): "))
    x = int(input("Enter the x-coordinate: "))
    y = int(input("Enter the y-coordinate: "))
    t = turtle.Turtle()
    tridecagonTurtle(s, x, y, t)
    turtle.done()

if __name__ == "__main__":
    main()
