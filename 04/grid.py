import turtle

count = 6

x = -200
y = -200

turtle.penup()
turtle.goto(x, y)
turtle.pendown()
while(count>0):
    turtle.forward(500)
    y += 100
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    count-=1

count = 6
y = -200

turtle.penup()
turtle.goto(x, y)
turtle.left(90)
turtle.pendown()
while(count>0):
    turtle.forward(500)
    x += 100
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    count-=1

turtle.exitonclick()
