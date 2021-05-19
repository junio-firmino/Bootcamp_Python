from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
grup_turtles = []
is_race_on = False

position = -100
for turtles in range(0,6):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.goto(x=-220, y=position)
    position += 50
    tim.color(colors[turtles])
    grup_turtles.append(tim)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in grup_turtles:
        if turtle.xcor() = 220:
            is_race_on = False
            winning_color = turtle.pencolor()




screen.exitonclick()

