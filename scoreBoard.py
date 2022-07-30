import turtle as t

class Score(t.Turtle):
    def __init__(self):
        super().__init__()

        self.color('white')
        self.penup()
        self.hideturtle()

        # Attributes
        self.l_score = 0
        self.r_score = 0
        self.update()
    
    def update(self):
        self.clear()
        # Writing/Displaying the score.
        self.goto(-100, 200)  # to write score of l_player.
        self.write(self.l_score, align='center', font=('Courier', 70, 'normal'))
        self.goto(100, 200)  # to write score of l_player.
        self.write(self.r_score, align='center', font=('Courier', 70, 'normal'))
        