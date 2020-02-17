# Lucas Traynor
# CSCI 1060-02
# this program uses turtle to create an image with colors 

import turtle


def main():
    main_square()
    top_left()
    top_right()
    bottom_right()
    bottom_left()
    center()
    text()
    turtle.done()

def main_square():
    turtle.fillcolor('blue')
    turtle.begin_fill()
    turtle.forward(500)
    turtle.right(90)
    turtle.forward(250)
    turtle.right(90)
    turtle.forward(500)
    turtle.right(90)
    turtle.forward(250)
    turtle.end_fill()


def top_left():
    turtle.fillcolor('black')
    turtle.begin_fill()
    turtle.right(90)
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(50)
    turtle.end_fill()

def top_right():
    turtle.goto(500,0)
    turtle.fillcolor('green')
    turtle.begin_fill()
    turtle.left(90)
    turtle.forward(150)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(150)
    turtle.left(90)
    turtle.forward(50)
    turtle.end_fill()

def bottom_right():
    turtle.goto(500,-250)
    turtle.fillcolor('red')
    turtle.begin_fill()
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(150)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(150)
    turtle.end_fill()

def bottom_left():
    turtle.goto(0,-250)
    turtle.fillcolor('black')
    turtle.begin_fill()
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(150)
    turtle.end_fill()
    turtle.penup()

def center():
    turtle.goto(150,-100)
    turtle.pencolor('black')
    turtle.fillcolor('purple')
    turtle.begin_fill()
    turtle.right(90)
    turtle.right(90)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(50)
    turtle.end_fill()

def text():
    turtle.goto(55,-35)
    turtle.pencolor('white')
    turtle.write("Top Left", font=("Arial", 16, "normal"))
    turtle.goto(385,-35)
    turtle.pencolor('black')
    turtle.write("Button Widget", font=("Arial", 16, "normal"))
    turtle.goto(395,-235)
    turtle.write("Bottom Right", font=("Arial", 16, "normal"))
    turtle.goto(40,-235)
    turtle.pencolor('yellow')
    turtle.write("Bottom Left", font=("Arial", 16, "normal"))
    turtle.goto(200,-132)
    turtle.pencolor('white')
    turtle.write("Label Widget", font=("Arial", 16, "normal"))



main()