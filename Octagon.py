# Heptagon=8
# angle(45)
import turtle
p=turtle.Screen()
p.bgcolor("green")
pen=turtle.Turtle()
pen.color("white")
for i in range(8):
    pen.forward(100)
    pen.right(45)
turtle.exitonclick()