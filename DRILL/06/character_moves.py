from pico2d import *
from math import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 0
y = 90
while (True):
    while (x < 800):
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(x,y)
            x = x + 2
            delay(0.01)

    while (y < 600):
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(x,y)
            y = y + 2
            delay(0.01)

    while (x > 0):
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(x,y)
            x = x - 2
            delay(0.01)

    while (y > 90):
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(x,y)
            y = y - 2
            delay(0.01)

    while (x < 400):
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(x,y)
            x = x + 2
            delay(0.01)

    x = 0
    while (x < 360):
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(cos((270 + x) / 360*2*pi) * 270 + 400,sin((270 + x) / 360*2*pi) * 270 + 345)
            x = x + 2
            delay(0.01)
    x = 400

close_canvas()


