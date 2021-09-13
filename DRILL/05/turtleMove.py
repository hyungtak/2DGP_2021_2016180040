import turtle as t
import random as r

def movew():
    t.setheading(90)
    t.forward(50)
    t.stamp()
    
def movea():
    t.setheading(180)
    t.forward(50)
    t.stamp()
    
def moves():
    t.setheading(270)
    t.forward(50)
    t.stamp()
    
def moved():
    t.setheading(0)
    t.forward(50)
    t.stamp()

def escape():
    t.goto(0,0)
    t.reset()

t.shape('turtle')

t.onkey(movew, 'w')
t.onkey(movea, 'a')
t.onkey(moves, 's')
t.onkey(moved, 'd')
t.onkey(escape, 'Escape')
t.listen()
