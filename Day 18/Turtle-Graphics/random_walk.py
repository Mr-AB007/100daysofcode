import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
########### Challenge 4 - Random Walk ########
directions = [0, 90, 180, 270]
tim.pensize(10)
tim.speed("fastest")

def random_colors():
    return (random.randint(0,255),random.randint(0,255),random.randint(0,255))

for _ in range(200):
    tim.color(random_colors())
    tim.forward(30)
    tim.setheading(random.choice(directions))