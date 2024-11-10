from turtle import *
from random import randint
interdraw = Turtle()
t = Turtle()
t.pensize(5)
t.shape('circle')
t.colormode(255)
def red():
    t.color('red')
def yellow():
    t.color('yellow')
def random_color():
    t.color(randint(0,255), randint(0,255), randint(0,255))
def right():
    pos = t.pos()
    t.goto(pos[0] + 10, pos[1])

def left():
    pos = t.pos()
    t.goto(pos[1], pos[0] + 10)

def up():
    pos = t.pos()
    t.goto(pos[0] + 10, pos[0])

def down():
    pos = t.pos()
    t.goto(pos[1] - 10, pos[0])





screen = getscreen()
screen.listen()
screen.onkey(red,'R')
screen.onkey(yellow,'Y')
screen.onkey(right, 'Right')
screen.onkey(random_color,'F')
screen.onkey(left, 'Left')
screen.onkey(up, 'Up')
screen.onkey(down, 'Down')
