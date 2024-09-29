import random
import  turtle as t

turtle = t.Turtle()
t.colormode(255)

turtle.speed("fast")

def random_colors():
    return random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)

def sinography(gap_size):
    for _ in range(int(360/gap_size)):
        turtle.color(random_colors())
        turtle.setheading(turtle.heading()+gap_size)
        turtle.circle(80)


sinography(10)
