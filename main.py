# Pong in Python 3
# https://www.youtube.com/watch?v=C6jJg9Zan7w
# Improvements: the paddles shouldn't be able to go off the screen
# The ball should progressively move faster after a certain number of paddle hits
# Install a menu/score screen
# Add pause and exit because program throws on exit
# Randomize starting vector and direction (including when a player scores)

import turtle
import os
from time import sleep

if os.name == "nt":
    import winsound

wnd = turtle.Screen()
wnd.title("Pong by Uncle Nick")
wnd.bgcolor("black")
wnd.setup(width=800, height=600)
wnd.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
RECTANGULAR_MOVE = .09
ball.dx = RECTANGULAR_MOVE
ball.dy = -RECTANGULAR_MOVE

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("{}  |  {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))


# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Keyboard binding
wnd.listen()
wnd.onkeypress(paddle_a_up, "w")
wnd.onkeypress(paddle_a_down, "s")
wnd.onkeypress(paddle_b_up, "Up")
wnd.onkeypress(paddle_b_down, "Down")

wnd.update()
# sleep(2)

# Main game loop
while True:
    wnd.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Check collision with border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        if os.name == "nt":
            winsound.PlaySound("Assets/pong_blip.wav", winsound.SND_ASYNC)
        else:
            os.system("aplay pong_blip.wav&")

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        if os.name == "nt":
            winsound.PlaySound("Assets/pong_blip.wav", winsound.SND_ASYNC)
        else:
            os.system("aplay pong_blip.wav&")

    # score
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("{}  |  {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("{}  |  {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collision
    if (330 < ball.xcor() < 350) and (paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(330)
        ball.dx *= -1
        if os.name == "nt":
            winsound.PlaySound("Assets/pong_blip.wav", winsound.SND_ASYNC)
        else:
            os.system("aplay pong_blip.wav&")

    if (-330 > ball.xcor() > -350) and (paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-330)
        ball.dx *= -1
        if os.name == "nt":
            winsound.PlaySound("Assets/pong_blip.wav", winsound.SND_ASYNC)
        else:
            os.system("aplay pong_blip.wav&")
