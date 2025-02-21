from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


snakes_position = [(0, 0), (-20, 0), (-40, 0)]
segments = []

for snake in snakes_position:
    new_snake = Turtle(shape="square")
    new_snake.penup()
    new_snake.color("white")
    new_snake.goto(snake)
    segments.append(new_snake)


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    # moving the last segment
    # for seg_num in range(start= 2, stop= 0, step= 1):
    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)

    # moving the first segment
    segments[0].forward(20)
    segments[0].left(90)























screen.exitonclick()