from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):

        for snake in STARTING_POSITIONS:
            new_snake = Turtle(shape="square")
            new_snake.penup()
            new_snake.color("white")
            new_snake.goto(snake)
            self.segments.append(new_snake)

    def move(self):
        # moving the last segment
        # for seg_num in range(start= 2, stop= 0, step= 1):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        # moving the first segment
        self.segments[0].forward(MOVE_DISTANCE)
        self.segments[0].left(90)
