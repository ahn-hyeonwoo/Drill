from pico2d import *
import game_world
import game_framework

MOVE_SPEED_PPS = 200

class Brick:
    def __init__(self):
        self.image = load_image('brick180x40.png')
        self.x, self.y = 800, 300
        self.dir = 1
        self.speed = MOVE_SPEED_PPS

    def get_bb(self):
        return self.x - 90, self.y - 20, self.x + 90, self.y + 20

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        # move 200 pixel per sec
        self.x += self.dir * self.speed * game_framework.frame_time
        if self.x >= 1600 or self.x <= 0: 
            self.dir *= -1
        pass

    def stop(self):
        # self.fall_speed = 0
        pass