import turtle as t

class Ball(t.Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()

        # Attributes to help with collisions and direction of motion.
        self.x_move = 10
        self.y_move = 10
        self.sleep_time = 0.1

    # Method to move the ball.
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    # Method to reverse y-direction of motion.
    def bounce(self):
        self.y_move *= (-1)  # reverse direction of motion along y-axis.

    def hit(self):
        self.x_move *= (-1)  # reverse direction of motion along y-axis.
        # Increase ball speed on each successful hit ==> decrease sleep_time.
        self.sleep_time *= (0.9)
    
    def reset_pos(self):
        self.sleep_time = 0.1  # reset ball speed on miss.
        self.goto(0, 0)
        self.x_move *= (-1)  # so that the player who scored has the turn to hit next.

