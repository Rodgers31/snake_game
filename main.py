from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")


snakes_y_postion = [-20, -40, -60]

for snake in snakes_y_postion:
    new_snake = Turtle(shape="square")
    new_snake.penup()
    new_snake.color("white")
    new_snake.goto(x=snake, y=0)






















screen.exitonclick()