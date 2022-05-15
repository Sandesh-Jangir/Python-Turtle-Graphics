import turtle
pen = turtle.Turtle()

# Configureation
pen.pensize(3)
pen.color('cyan')
turtle.bgcolor('black')
pen.hideturtle()
pen.speed(100)

# Generating Pattern
i = 0
while i < 200:
    pen.penup()
    pen.forward(i+5)
    pen.right(90)
    pen.pendown()
    pen.circle(i+10)
    i=i+1

turtle.done()