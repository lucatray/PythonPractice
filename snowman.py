# Lucas Traynor
# # 4/27/18
# this program creates a snowman using turtle graphics

import turtle


def main():

    draw_circle()
    draw_snowman()
    draw_rectangle()

    turtle.done()



def draw_circle():
        turtle.penup()
        turtle.goto(0, -200)
        turtle.fillcolor('blue')
        turtle.begin_fill()
        turtle.circle(100)
        turtle.end_fill()
        turtle.done()

def draw_snowman():
    turtle.goto(0,0)
    turtle.pendown()
    turtle.circle(.6 * 100)
    turtle.penup()
    turtle.goto(0,120)
    turtle.pendown()
    turtle.circle(.4 * 100)
    turtle.penup()
    turtle.goto(-15, 175)
    turtle.fillcolor('black')
    turtle.begin_fill()
    turtle.circle(5)
    turtle.end_fill()
    turtle.goto(15, 175)
    turtle.fillcolor('black')
    turtle.begin_fill()
    turtle.circle(5)
    turtle.end_fill()
    turtle.goto(-15,145)
    turtle.fillcolor('black')
    turtle.begin_fill()
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(2)
    turtle.right(90)
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(2)
    turtle.end_fill()
    turtle.hideturtle()

def draw_rectangle():
    turtle.goto(0,190)
    turtle.fillcolor('black')
    turtle.begin_fill()
    turtle.right(90)
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(15)
    turtle.left(90)
    turtle.forward(15)
    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(15)
    turtle.left(90)
    turtle.forward(15)
    turtle.end_fill()




main()