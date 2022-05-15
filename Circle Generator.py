import turtle
import random
noc = int(input("Enter No. of circle to generate randomly: \n"))
pen = turtle.Turtle()

pen.pensize(5)
pen.hideturtle()

colors = ["red", "cyan", "magenta", "blue", 'green', "black"]

for i in range (noc):
    # Setting Random Position
    xcord = random.randrange(-200, 200)
    ycord = random.randrange(-200, 200)
    pen.penup()
    pen.setpos(xcord, ycord)
    pen.pendown()

    # Creating circle
    pen.color('black', colors[random.randint(0, 5)])
    pen.begin_fill()
    pen.circle(random.randrange(10, 200))
    pen.end_fill()


turtle.done()