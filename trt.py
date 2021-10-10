from turtle import *
from random import *

win = Screen()
bob = Turtle()
win.colormode(255)
bob.speed(0)
bob.width(2)
win.bgcolor(50, 0, 70)
bob.pencolor(255, 255, 0)

def shape(angle, side, limit):
    revers = 200
    bob.pencolor(randint(50, 255), randint(50, 255), randint(50, 255))
    bob.forward(side)
    if side % (revers * 2) == 0:
        angle += 2
    elif side % revers == 0:
        angle -= 2
    bob.right(angle)
    side += 2
    if side < limit:
        shape(angle, side, limit)

angle = 119
side = 0
limit = 600
shape(angle, side, limit)

mainloop()

