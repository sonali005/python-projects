import turtle
turtle.speed(10)
def square():
    counter=0
    row=0
    turtle.penup()
    turtle.goto(-300,300)
    turtle.pendown()
    while row<20:
        while counter<4:
            turtle.forward(30)
            turtle.left(90)
            counter=counter+1
        counter=0
        turtle.forward(30)
        row=row+1
    input('.')
square()