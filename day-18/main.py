from turtle import Turtle, Screen
import random


tim = Turtle()
tim.shape("arrow")
tim.color("navy")

colours = ["navy", "blue", "green", "yellow", "lime", "orange", "brown", "dark cyan"]
sides = 3
degree = 360
start_to_draw = True

while start_to_draw:
    angle_size = degree / sides
    tim.color(random.choice(colours))
    for _ in range(sides):
        tim.fd(100)
        tim.right(angle_size)
    sides += 1
    print(sides, angle_size)

    if sides == 12:
        start_to_draw = False



screen = Screen()
screen.exitonclick()