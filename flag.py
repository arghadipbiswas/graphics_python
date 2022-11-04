from turtle import*
pensize(3)
def rectangle(color):
    begin_fill()
    fillcolor(color)
    for i in range(2):
        forward(300)
        right(90)
        forward(50)
        right(90)
    end_fill()
up()
goto(0,-200)
down()
goto(0,300)
rectangle("orange")
goto(0,250)
rectangle("white")
goto(0,200)
rectangle("green")
up()
goto(150,250)
down()
circle(-25)
right(90)
up()
goto(150,225)
down()
for i in range(21):
    color("blue")
    forward(23)
    back(23)
    left(17)
hideturtle()













# from turtle import *
# bgcolor("black")
# width(2)
# speed(50)

# for i in range(11):
#     for colors in ("red" , "magenta" , "blue" , "cyan" , "green" , "yellow" ,"orange"):
#         color(colors)
#         circle(100)
#         left(5)

# exitonclick()