import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

py = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(py.up, "Up")
screen.onkey(py.down, "Down")
screen.onkey(py.left, "Left")
screen.onkey(py.right, "Right")

slithering = True
while slithering:
    screen.update()
    time.sleep(0.15)
    py.move()

    # Detect collision with food
    if py.head.distance(food) < 15:
        food.random_color()
        food.refresh()
        py.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if py.head.xcor() > 320 or py.head.xcor() < -320 or py.head.ycor() > 320 or py.head.ycor() < -320:
        scoreboard.reset()
        py.reset()

    # Detect collision with tail
    for segment in py.segments[1:]:
        if py.head.distance(segment) < 10:
            scoreboard.reset()
            py.reset()

screen.exitonclick()
