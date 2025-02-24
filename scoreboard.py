from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 9, 'normal')


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.my_score()
        self.hideturtle()

    def my_score(self):
        self.clear()
        self.goto(0, 280)
        self.color('white')
        self.write(arg=f"Score: {self.current_score}", align=ALIGNMENT, font=FONT)
        self.current_score += 1


