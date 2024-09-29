import turtle as t
from turtle import Screen

timmy_the_turtle = t.Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")


def draw_rectangle():
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(90)
    timmy_the_turtle.forward(50)
    timmy_the_turtle.left(90)
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(90)
    timmy_the_turtle.forward(50)

draw_rectangle()




screen = Screen()
screen.exitonclick()