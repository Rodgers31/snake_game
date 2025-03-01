from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 13, 'normal')


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.high_score = 0
        self.my_score()
        self.hideturtle()

    def my_score(self):
        self.clear()
        self.goto(0, 280)
        self.color('white')
        self.write(arg=f"Score: {self.current_score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
        self.current_score += 1

    def reset(self):
        if self.current_score > self.high_score:
            self.high_score = self.current_score
        self.current_score = 0
        self.my_score()
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg="Game over.", align=ALIGNMENT, font=FONT)


