import turtle as t
import time
import paddleClass as pC
import ballClass as bC

# Setting up the screen.
screen = t.Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')
screen.tracer(0)  # Turn off animations.

# Creating Paddle objects using Paddle class.
r_paddle = pC.Paddle(350, 0)
l_paddle = pC.Paddle(-350, 0)

# Moving the paddles.
screen.listen()
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')

# Creating a Ball object using Ball class.
ball = bC.Ball()

game_on = True
while game_on:
    time.sleep(0.1)  # To slow down the ball.
    screen.update()  # To make paddle visible, since tracer(0) (animations are off).
    # Move the ball.
    ball.move()


screen.exitonclick()
