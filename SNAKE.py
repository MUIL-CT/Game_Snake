import turtle
import random
import math

__Pen = turtle.Pen()


def GenerateMap():
    turtle.bgcolor("#ffffff")
    __Pen.pencolor("#000099")
    Create_Pen_Egg()
    __Pen.penup()
    __Pen.goto((-150), (-150))
    __Pen.pendown()
    for __count in range(4):
        __Pen.forward(300)
        __Pen.left(90)
    __Pen.penup()
    __Pen.goto(0, 0)
    GenerateEgg()
    return 0

def Create_Pen_Egg():
    egg_pen.pencolor("#ff0000")
    egg_pen.penup()
    egg_pen.hideturtle()

def Left():
    __Pen.setheading(180)
    return 0

def Right():
    __Pen.setheading(0)
    return 0

def GenerateEgg():
    egg_pen.clear()
    egg_pen.goto(random.randint((-145), 145), random.randint((-145), 145))
    egg_pen.dot(5)

def Up():
    __Pen.setheading(90)
    return 0

def Down():
    __Pen.setheading(270)
    return 0

def CheckFrameCollide():
    if (__Pen.xcor() > 150 or __Pen.xcor() <= -150 or __Pen.ycor() > 150 or __Pen.ycor() <= -150):
        print('Collided!')
        GameLabel()
        turtle.done()
    return 0

def CheckEggCollide():
    if (math.sqrt((__Pen.xcor() - egg_pen.xcor()) ** 2 + (__Pen.ycor() - egg_pen.ycor()) ** 2) >= -2 and math.sqrt((__Pen.xcor() - egg_pen.xcor()) ** 2 + (__Pen.ycor() - egg_pen.ycor()) ** 2) <= 2):
        print('+1 Point!')
        __Pen.write('x')
        GenerateEgg()
        return 1
    return 0

def GenerateScoreLabel():
    text_scores.hideturtle()
    text_scores.penup()
    text_scores.pencolor("#33cc00")
    return 0

def GenerateGameLabel():
    text_gameover.hideturtle()
    text_gameover.penup()
    text_gameover.pencolor("#cc0000")
    return 0

def ScoreLabel(scores):
    text_scores.clear()
    text_scores.goto(140, 150)
    text_scores.write(scores, font = ('Arial', 15, 'bold'))
    return 0

def GameLabel():
    text_gameover.clear()
    text_gameover.goto(0, 150)
    text_gameover.write('GAMEOVER!', font = ('Arial', 15, 'bold'))
    return 0

#Get start with Python
speed = 1
scores = 0
egg_pen = turtle.Pen()
text_scores = turtle.Pen()
text_gameover = turtle.Pen()
GenerateGameLabel()
GenerateScoreLabel()
GenerateMap()
while True:
    CheckFrameCollide()
    if (CheckEggCollide() == 1):
        scores += 1
        speed += 0.05
        ScoreLabel(scores)
        print('Score = ',scores)
    __Pen.forward(speed)
    turtle.onkey(Up, "Up")
    turtle.onkey(Down, "Down")
    turtle.onkey(Left, "Left")
    turtle.onkey(Right, "Right")
    turtle.listen()
turtle.done()
