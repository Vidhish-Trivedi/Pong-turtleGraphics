import turtle as t

# Creating a paddle.
class Paddle(t.Turtle):
    def __init__(self, xc, yc):
        super().__init__()  # initialising properties of Turtle() class, which is inherited by Paddle class.
        # paddle = t.Turtle()  # already inherited.
        # paddle.hideturtle()  # not required if tracer(0) is used.
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1) # 20x5 = 100, 20x1 = 20 : new size = 100 by 20.
        self.color('white')
        self.penup()
        self.goto(xc, yc)
        # paddle.showturtle()  # not required if tracer(0) is used.

    # Function to move paddle up.
    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    # Function to move paddle down.
    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)