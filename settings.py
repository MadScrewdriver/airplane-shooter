import pygame, os
from screeninfo import get_monitors
from Basic_Component import BasicComponent


class Score:
    def __init__(self):
        self.score = 0

    def add_score(self):
        self.score += 10

    def get_score(self):
        return self.score


class GlobalConstants:
    b_a_path = os.path.join("Pictures", "Player", "BasicAirplane")
    MARGIN = int(get_monitors()[0].height * 0.025)
    SCREEN_LENGTH = int(get_monitors()[-1].height * 0.75)
    SCREEN_WITH = int(get_monitors()[-1].height * 0.5)
    SCREEN = pygame.display.set_mode((SCREEN_WITH, SCREEN_LENGTH))
    ENEMIES = []
    BULLETS = []
    BULLET_SIZE = int(SCREEN_WITH / 54)
    PLAYER_PNGS = (lambda x=b_a_path: [os.path.join(x, p + ".png") for p in ["straight", "left", "right"]])()
    PLAYER = BasicComponent(SCREEN_WITH / 2 - (SCREEN_WITH / 3.90) / 2, SCREEN_LENGTH * (4 / 6),
                            SCREEN_WITH / 3.90, SCREEN_WITH / 5.27, PLAYER_PNGS, SCREEN)


class BulletConstants(GlobalConstants):
    def __init__(self):
        self.BULLET_SPEED = -self.SCREEN_WITH / 80


class RocketConstants(GlobalConstants):
    def __init__(self):
        self.SPEED = self.SCREEN_WITH / 120


class EnemiesConstants(GlobalConstants):
    def __init__(self):
        self.ENEMY_WITH = self.SCREEN_WITH / 3.90
        self.ENEMY_HEIGHT = self.SCREEN_WITH / 5.27
        self.ENEMY_SPEED = self.SCREEN_WITH / 180


class BackgroundConstants(GlobalConstants):
    def __init__(self):
        self.BG_SPEED = self.SCREEN_WITH / 270
