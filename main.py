from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(height=400, width=500)
user_input = (screen.textinput(title="Make your bet", prompt="Which turtle will win?"))

colours = ["red", "orange", "blue", "yellow","green", "purple"]

tim = []

for i in range(len(colours)):
    new_turtle = Turtle(shape="turtle")
    tim.append(new_turtle)
    tim[i].penup()
    tim[i].color(colours[i])
    tim[i].goto(x=-230, y=(-80 + i*30))
    # x has been kept as 230 because the turtle has a size of 40*40.So we subtract half of the width of the turtle from
    # the actual window size.

if user_input:
    is_race_on = True

while is_race_on:
    for i in range(len(tim)):
        if tim[i].xcor() > 230:
            is_race_on = False
            winning_turtle = tim[i].pencolor()
            if winning_turtle == user_input:
                print(f"You win. The winning turtle is {winning_turtle}")
            else:
                print(f"You lost. The winning turtle is {winning_turtle}")

        random_distance = random.randint(0, 10)
        tim[i].forward(random_distance)

screen.exitonclick()
