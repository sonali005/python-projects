from turtle import Screen, Turtle

turtle = Turtle()
t = Screen()

#draw a circle 
turtle.right(90)
turtle.circle(50, 180)
turtle.left(90)
turtle.forward(100)

t.exitonclick()
turtle.done()