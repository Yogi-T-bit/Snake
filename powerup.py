# powerup.py

import pygame
import random
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, BLUE, SNAKE_SIZE

class Powerup:
    def __init__(self):
        self.__position = self.generate_position()
        self.__type = random.choice(["speed_boost", "score_multiplier"])

    def generate_position(self):
        x = random.randrange(0, SCREEN_WIDTH - SNAKE_SIZE, SNAKE_SIZE)
        y = random.randrange(0, SCREEN_HEIGHT - SNAKE_SIZE, SNAKE_SIZE)
        return x, y

    def draw(self, screen):
        pygame.draw.rect(screen, BLUE, (self.__position[0], self.__position[1], SNAKE_SIZE, SNAKE_SIZE))

    def apply_powerup(self, snake):
        if self.__type == "speed_boost":
            snake.increase_speed()
        elif self.__type == "score_multiplier":
            snake.increase_score_multiplier()

    def get_position(self):
        return self.__position
