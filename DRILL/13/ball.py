import random
from pico2d import *
import game_world
import game_framework


class Ball:
    MIN_FALL_SPEED = 50  # 50 pps = 1.5 meter per sec
    MAX_FALL_SPEED = 400 # 200 pps = 6 meter per sec
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y, self.fall_speed = random.randint(0, 1600-1), 600, random.randint(Ball.MIN_FALL_SPEED, Ball.MAX_FALL_SPEED)
        self.collideonbrick = False
        self.speed = 200

    def get_bb(self):
        # fill here
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw(self):
        self.image.draw(self.x, self.y)
        # fill here
        draw_rectangle(*self.get_bb())

    def update(self):
        if self.collideonbrick:
            self.x += game_framework.frame_time * self.speed
            if self.x > 1600:
                self.x = 1600
                self.speed = -self.speed
            if self.x < 0:
                self.x = 0
                self.speed = -self.speed
        else:
            self.y -= self.fall_speed * game_framework.frame_time

    def stop(self):
        self.fall_speed = 0

    def stopandmove(self):
        self.collideonbrick = True


