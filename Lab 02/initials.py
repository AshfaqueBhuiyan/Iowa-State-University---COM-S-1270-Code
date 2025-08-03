# Ash Bhuiyan                                       06-25-2025
# Lab 2 - Drawing name initials using Python's turtle library.

# CITATION - URL: https://docs.python.org/3/library/turtle.html#turtle.color
# CITATION - Authors: Python Software Foundation
# CITATION - Date Updated: 06-24-2025
# CITATION - Date Accessed: 06-24-2025

import turtle

# Background
screen = turtle.Screen()
screen.bgcolor("lavender")

pen = turtle.Turtle()
pen.pensize(12)
pen.speed(2)

# Firstname letter
pen.color("navy", "lavender")
pen.penup()
pen.goto(-120, -50)
pen.pendown()
pen.begin_fill()
pen.left(75)
pen.forward(100)
pen.right(150)
pen.forward(100)
pen.backward(40)
pen.right(105)
pen.forward(35)
pen.end_fill()

# Lastname letter
pen.penup()
pen.setheading(0)
pen.goto(20, -50)
pen.pendown()
pen.color("darkgreen", "lavender")
pen.begin_fill()
pen.left(90)
pen.forward(100)
pen.right(90)
pen.circle(-25, 180)
pen.right(180)
pen.circle(-25, 180)
pen.end_fill()
pen.hideturtle()
screen.mainloop()
