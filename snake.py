# snake.py

import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, GREEN, SNAKE_SIZE, SNAKE_SPEED, HIGH_SCORE_FILE

class Snake:
    def __init__(self):
        self.__body = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
        self.__direction = "right"
        self.__speed = SNAKE_SPEED
        self.__score = 0
        self.__high_score = 0
        self.__game_over = False
        self.__load_high_score()

    def __load_high_score(self):
        try:
            with open(HIGH_SCORE_FILE, "r") as file:
                self.__high_score = int(file.read())
        except FileNotFoundError:
            self.__high_score = 0

    def __save_high_score(self):
        with open(HIGH_SCORE_FILE, "w") as file:
            file.write(str(self.__high_score))

    def update(self):
        if not self.__game_over:
            head = self.__body[0]
            x, y = head

            if self.__direction == "up":
                y -= self.__speed
            elif self.__direction == "down":
                y += self.__speed
            elif self.__direction == "left":
                x -= self.__speed
            elif self.__direction == "right":
                x += self.__speed

            new_head = (x, y)

            # Check for self-collision
            if new_head in self.__body[1:]:
                self.__game_over = True

                # Update high score if needed
                if self.__score > self.__high_score:
                    self.__high_score = self.__score
                    self.__save_high_score()

            self.__body.insert(0, new_head)
            self.__body = self.__body[:-1]

    def change_direction(self, new_direction):
        opposite_directions = {
            "up": "down",
            "down": "up",
            "left": "right",
            "right": "left",
        }

        if new_direction != opposite_directions[self.__direction]:
            self.__direction = new_direction

    def draw(self, screen):
        for segment in self.__body:
            pygame.draw.rect(screen, GREEN, (segment[0], segment[1], SNAKE_SIZE, SNAKE_SIZE))

    def get_speed(self):
        return self.__speed + len(self.__body) // 5

    def get_score(self):
        return self.__score

    def increase_score(self):
        self.__score += 1

    def grow(self):
        tail = self.__body[-1]
        x, y = tail

        if self.__direction == "up":
            y += SNAKE_SIZE
        elif self.__direction == "down":
            y -= SNAKE_SIZE
        elif self.__direction == "left":
            x += SNAKE_SIZE
        elif self.__direction == "right":
            x -= SNAKE_SIZE

        self.__body.append((x, y))

    def play_eat_sound(self):
        # Placeholder method; add sound functionality as needed
        pass

    def get_body(self):
        return self.__body

    def is_game_over(self):
        return self.__game_over

    def get_high_score(self):
        return self.__high_score
