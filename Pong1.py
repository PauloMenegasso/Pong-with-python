import turtle
import winsound
import random

window = turtle.Screen()
window.title("Pong")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# score
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
ball.dx = 0.1
ball.dy = -0.1


# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A:0  PlayerB:0", align="center",
          font=("Courier", 24, "normal"))

# Functions


def reset_ball_position():
    ball.goto(0, random.randint(-300, 300))


def colision_sound():
    winsound.PlaySound("sound/colision.wav", winsound.SND_ASYNC)


def score_sound():
    winsound.PlaySound("sound/score.wav", winsound.SND_ASYNC)


def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)
    if paddle_a.ycor() > 270:
        paddle_a.sety(270)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)
    if paddle_a.ycor() < -270:
        paddle_a.sety(-270)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)
    if paddle_b.ycor() > 270:
        paddle_b.sety(270)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)
    if paddle_b.ycor() < -270:
        paddle_b.sety(-270)


# Keyboard binding
window.listen()
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    window.update()

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        colision_sound()

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        colision_sound()

    if ball.xcor() > 390:
        reset_ball_position()
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A:{}  PlayerB:{}".format(score_a, score_b), align="center",
                  font=("Courier", 24, "normal"))
        score_sound()

    if ball.xcor() < -390:
        reset_ball_position()
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A:{}  PlayerB:{}".format(score_a, score_b), align="center",
                  font=("Courier", 24, "normal"))
        score_sound()

    # paddle B Colision
    if ball.xcor() > 340 and ball.xcor() < 360 and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
        colision_sound()

    # paddle A Colision
    if ball.xcor() < -340 and ball.xcor() > -360 and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
        colision_sound()
