import game_framework
from pico2d import *
import random

import game_world

# Bird Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Bird Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14

class BirdRunState:

    def enter(bird, event):
        #0일때 좌측 진행
        if (random.randint(1, 100) // 2) == 0:
            bird.velocity -= RUN_SPEED_PPS
        else:
            bird.velocity += RUN_SPEED_PPS

        bird.dir = clamp(-1, bird.velocity, 1)

    def exit(bird, event):
        pass

    def do(bird):
        bird.frame = (bird.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14
        bird.x += bird.velocity * game_framework.frame_time
        bird.x = clamp(25, bird.x, 1600 - 25)
        if bird.x >= 1550:
            bird.velocity -= RUN_SPEED_PPS * 2
        if bird.x <= 35:
            bird.velocity += RUN_SPEED_PPS * 2

        bird.dir = clamp(-1, bird.velocity, 1)
    def draw(bird):
        if bird.dir == 1:
            bird.image.clip_draw(int(bird.frame) * 100, 0, 100, 100, bird.x, bird.y)
        else:
            bird.image.clip_composite_draw(int(bird.frame) * 100, 0, 100, 100, 0, 'h', bird.x, bird.y, 100, 100)


class Bird:
    image = None

    def __init__(self):
        self.x, self.y = 1600 // 2 + random.randint(10, 200), 300 + random.randint(-200, 200)
        # Boy is only once created, so instance image loading is fine
        if self.image == None:
            self.image = load_image('bird100x100x14.png')
        self.dir = 1
        self.velocity = 0
        self.frame = random.randint(0, 14)
        self.event_que = []
        self.cur_state = BirdRunState
        self.cur_state.enter(self, None)

    def get_bb(self):
        # fill here
        return 0, 0, 0, 0

    def add_event(self, event):
        pass

    def update(self):
        self.cur_state.do(self)

    def draw(self):
        self.cur_state.draw(self)

    def handle_event(self, event):
        pass
