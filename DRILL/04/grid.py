import turtle as t

t.shape("turtle")
t.penup()

t.setposition(-250,250)
t.pendown()

t.setheading(0)
for i in range(6):
    for j in range(4):
        t.forward(i*100)
        t.right(90)

t.penup()
t.setposition(250,-250)
t.pendown()
t.setheading(180)
for i in range(6):
    for j in range(4):
        t.forward(i*100)
        t.right(90)

t.hideturtle()
    
t.done()
