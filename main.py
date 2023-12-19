# main.py

import pygame
from pygame.locals import *
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from snake import Snake
from food import Food

def draw_scores(screen, score, speed):
    font = pygame.font.SysFont(None, 24)
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    speed_text = font.render(f"Speed: {speed}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    screen.blit(speed_text, (10, 30))

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Snake Game")
    clock = pygame.time.Clock()

    # Load background image
    background_image = pygame.image.load("background_image1.jpg")  # Change the filename to your image file
    background_rect = background_image.get_rect()

    snake = Snake()
    food = Food()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    snake.change_direction("up")
                elif event.key == K_DOWN:
                    snake.change_direction("down")
                elif event.key == K_LEFT:
                    snake.change_direction("left")
                elif event.key == K_RIGHT:
                    snake.change_direction("right")

        snake.update()

        if snake.get_body()[0] == food.get_position():
            snake.grow()
            food.set_position(food.generate_position())
            snake.increase_score()

        # Blit the background image
        screen.blit(background_image, background_rect)

        snake.draw(screen)
        food.draw(screen)
        draw_scores(screen, snake.get_score(), snake.get_speed())
        pygame.display.update()

        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
