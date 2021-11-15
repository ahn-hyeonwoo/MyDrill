import random
from pico2d import *
import game_world
import game_framework


PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 123  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 3
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14


class Bird:
    def __init__(self):
        self.image = load_image('bird100x100x14.png')
        self.x, self.y, self.speed = random.randint(100, 1500), random.randint(300, 500), RUN_SPEED_PPS
        self.frame = random.randint(0, 13)
        self.dir = random.randint(0, 1)
        if self.dir == 0:
            self.dir = -1

    # def get_bb(self):
    #     # fill here
    #     return 0,0,0,0

    def draw(self):
        self.image.clip_draw(int(self.frame) * 100, 0, 100, 100, self.x, self.y)
        # boy.image.clip_draw(int(boy.frame) * 100, 100, 100, 100, boy.x, boy.y)

    def update(self):
        # self.y -= self.fall_speed * game_framework.frame_time
        self.x += self.speed * self.dir * game_framework.frame_time
        if self.x > 1600:
            self.dir *= -1
            self.x = 1599
        elif self.x < 0:
            self.dir *= -1
            self.x = 1

        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14

# 비둘기의 속도는 평균 123km입니다.
# 출처: https://www.ytn.co.kr/_ln/0104_201905131122012523
# 제가 봤던 비둘기들은 1초에 약 3번정도 날갯짓을 했었습니다.