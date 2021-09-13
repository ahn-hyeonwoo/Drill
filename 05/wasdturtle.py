import turtle

def reset():
    turtle.reset()

def goright():
    turtle.stamp()
    turtle.setheading(0)
    turtle.forward(50)

def goleft():
    turtle.stamp()
    turtle.setheading(180)
    turtle.forward(50)

def goup():
    turtle.stamp()
    turtle.setheading(90)
    turtle.forward(50)

def godown():
    turtle.stamp()
    turtle.setheading(270)
    turtle.forward(50)

turtle.shape('turtle')

turtle.onkey(reset, 'Escape')
turtle.onkey(goright, 'd')
turtle.onkey(goleft, 'a')
turtle.onkey(goup, 'w')
turtle.onkey(godown, 's')
turtle.listen()
