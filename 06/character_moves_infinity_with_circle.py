from pico2d import *

import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 0
y = 90
circle = -90
while(True):
    while(x < 800):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x + 10
        delay(0.05)
    while(y < 600):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y = y + 10
        delay(0.05)
    while(x > 0):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x - 10
        delay(0.05)
    while(y > 90):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y = y - 10
        delay(0.05)
    while(x < 400):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x + 10
        delay(0.05)
    while(circle < 270):
        clear_canvas_now()
        grass.draw_now(400, 30)
        x = 400 + 255*math.cos(circle/360*2*math.pi)
        y = 345 + 255*math.sin(circle/360*2*math.pi)
        character.draw_now(x, y)
        circle += 3
        delay(0.05)
    circle = -90

close_canvas()