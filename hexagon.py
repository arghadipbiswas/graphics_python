#  Hexagon=6
# angle(60)
import turtle
p=turtle.Screen()
p.bgcolor("green")
pen=turtle.Turtle()
pen.color("white")
for i in range(6):
    pen.forward(100)
    pen.right(60)
turtle.exitonclick()