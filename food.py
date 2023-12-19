# food.py

import pygame
import random
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, RED, FOOD_SIZE, SNAKE_SIZE

class Food:
    def __init__(self):
        self.__position = self.generate_position()

    def generate_position(self):
        x = random.randrange(0, SCREEN_WIDTH - FOOD_SIZE, SNAKE_SIZE)
        y = random.randrange(0, SCREEN_HEIGHT - FOOD_SIZE, SNAKE_SIZE)
        return x, y

    def draw(self, screen):
        pygame.draw.rect(screen, RED, (self.__position[0], self.__position[1], FOOD_SIZE, FOOD_SIZE))

    def get_position(self):
        return self.__position

    def set_position(self, position):
        self.__position = position

    def check_collision(self, snake):
        return self.__position in snake.get_body()
