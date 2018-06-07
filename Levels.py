from random import *
from Messerschmitt import Messerschmitt
from Bomber import Bomber
from Settings import LevelsConstants


class Levels(LevelsConstants):
    def __init__(self):
        super().__init__()

    def level_1(self):
        self.ENEMIES.append(
            Messerschmitt(
                randint(int(self.MARGIN), int(self.SCREEN_WITH - (self.MARGIN + self.SCREEN_WITH / 3.90))),
                -self.ENEMY_HEIGHT))

    def level_2(self):
        self.ENEMIES.append(
            Messerschmitt(
                randint(int(self.MARGIN), int(self.SCREEN_WITH - self.MARGIN - self.ENEMY_WITH)),
                int(-1 * randint(self.ENEMY_HEIGHT, self.ENEMY_HEIGHT * 2))
                -self.ENEMY_HEIGHT))

        left = self.ENEMIES[0].x - self.MARGIN - self.MIN_DISTANCE >= self.ENEMY_WITH
        right = (self.SCREEN_WITH - self.MARGIN) - (
                    self.ENEMIES[0].x + self.ENEMY_WITH) - self.MIN_DISTANCE >= self.ENEMY_WITH

        if left and right:
            left = choice([True, False])

        if left:
            self.ENEMIES.append(
                Messerschmitt(
                    randint(int(self.MARGIN), int(self.ENEMIES[0].x - self.MIN_DISTANCE - self.ENEMY_WITH)),
                    int(-self.ENEMY_HEIGHT)
                    - self.ENEMY_HEIGHT))

        else:
            self.ENEMIES.append(
                Messerschmitt(
                    randint(int(self.ENEMIES[0].x + self.ENEMY_WITH + self.MIN_DISTANCE),
                    int(self.SCREEN_WITH - self.MARGIN - self.ENEMY_WITH)),
                    int(-self.ENEMY_HEIGHT)
                    - self.ENEMY_HEIGHT))

    def level_3(self):
        array = randint(1, 5)

        if array == 1:
            self.ENEMIES.append(
                Messerschmitt(
                    self.MARGIN,
                    -self.ENEMY_HEIGHT))

            self.ENEMIES.append(
                Messerschmitt(
                    self.MARGIN + self.ENEMY_WITH + self.MIN_DISTANCE,
                    int(-self.ENEMY_HEIGHT * 2)))

            self.ENEMIES.append(
                Bomber(
                    self.MARGIN + self.ENEMY_WITH * 2 + self.MIN_DISTANCE * 2,
                    int(-self.ENEMY_HEIGHT * 2 + -self.BOMBER_HEIGHT)))

        elif array == 2:
            self.ENEMIES.append(
                Messerschmitt(
                    self.SCREEN_WITH - self.MARGIN - self.ENEMY_WITH,
                    int(-self.ENEMY_HEIGHT)))

            self.ENEMIES.append(
                Messerschmitt(
                    self.SCREEN_WITH - self.MARGIN - self.ENEMY_WITH * 2 - self.MIN_DISTANCE,
                    int(-self.ENEMY_HEIGHT * 2)))

            self.ENEMIES.append(
                Bomber(
                    self.SCREEN_WITH - self.MARGIN - self.ENEMY_WITH * 3 - self.MIN_DISTANCE * 2,
                    int(-self.ENEMY_HEIGHT * 2 - self.BOMBER_HEIGHT)))

        elif array == 3:
            self.ENEMIES.append(
                Messerschmitt(
                    self.SCREEN_WITH / 2 - self.ENEMY_WITH / 2,
                    int(-self.ENEMY_HEIGHT)))

            self.ENEMIES.append(
                Bomber(
                    self.SCREEN_WITH / 2 - self.ENEMY_WITH / 2 - self.ENEMY_WITH - self.MIN_DISTANCE,
                    int(-self.ENEMY_HEIGHT - self.BOMBER_HEIGHT)))

            self.ENEMIES.append(
                Messerschmitt(
                    self.SCREEN_WITH / 2 + self.ENEMY_WITH / 2 + self.MIN_DISTANCE,
                    int(-self.ENEMY_HEIGHT * 2)))

        elif array == 5:
            self.ENEMIES.append(
                Bomber(
                    int(self.SCREEN_WITH / 2 - self.ENEMY_WITH / 2),
                    int(-self.ENEMY_HEIGHT - self.BOMBER_HEIGHT)))

            self.ENEMIES.append(
                Messerschmitt(
                    int(self.SCREEN_WITH / 2 - self.ENEMY_WITH / 2 - self.MIN_DISTANCE - self.ENEMY_WITH),
                    int(-self.ENEMY_HEIGHT)))

            self.ENEMIES.append(
                Messerschmitt(
                    int(self.SCREEN_WITH / 2 + self.ENEMY_WITH / 2 + self.MIN_DISTANCE),
                    int(-self.ENEMY_HEIGHT)))