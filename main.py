import turtle as t
import time
import paddleClass as pC
import ballClass as bC
import scoreBoard as sB

# Setting up the screen.
screen = t.Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')
screen.tracer(0)  # Turn off animations.

# Creating Paddle objects using Paddle class.
r_paddle = pC.Paddle(350, 0)
l_paddle = pC.Paddle(-350, 0)
# Creating a Ball object using Ball class.
ball = bC.Ball()
# Creating the scoreBoard using the Score class.
scoreboard = sB.Score()


# Moving the paddles.
screen.listen()
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')

game_on = True
while game_on:
    time.sleep(0.1)  # To slow down the ball.
    screen.update()  # To make paddle visible, since tracer(0) (animations are off).
    # Move the ball.
    ball.move()

    # Detect collisions with walls (top and bottom).
    if(ball.ycor() > 280 or ball.ycor() < -280):
        # Bounce the ball (change the direction along y-axis only).
        ball.bounce()
    
    # Detect collisions with paddle(s).
    # r_paddle or l_paddle.
    if((ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320)):
        ball.hit()

        # FIX: ball.hit() is called multiple times when dist remains
        #      within the constraints after collision.
    
    # Detect miss at paddle and reset ball to center.
    if(ball.xcor() > 380):  # right miss.
        ball.reset_pos()
        scoreboard.l_score += 1
        scoreboard.update()
    
    if(ball.xcor() < -380):  # left miss.
        ball.reset_pos()
        scoreboard.r_score += 1
        scoreboard.update()

screen.exitonclick()
