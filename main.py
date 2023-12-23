import turtle
import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput('Who will win?', prompt="Which turtle will win the race? Enter a color:")
print(user_bet)

is_race_on = False
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
for i in range(6):

    turtles.append(Turtle(shape="turtle",))
    turtles[i].penup()
    turtles[i].color(colors[i])
    turtles[i].goto(x=-225, y=50*i-125)

if user_bet:
    is_race_on=True

while is_race_on:
    for turtle in turtles:
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)
        if turtle.xcor() >230:
            print(turtle.pencolor())
            is_race_on = False
