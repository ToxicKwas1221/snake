import pygame
from pygame.locals import *
import random
import sys


# Settings
CAPTION = "Snake"
SNAKE_COLOR = (0, 255, 0)
BACKGROUD_COLOR = (53, 53, 53)
APPLE_COLOR = (255, 0, 0)


score = 0
taken_spaces = []
end_of_tail = None
pygame.init()
screen = pygame.display.set_mode((500, 500))
class Game:
    def __init__(self):
        pygame.display.set_caption(CAPTION)
        screen.fill((BACKGROUD_COLOR))
        pygame.display.update()
        self.snake = Snake()
        self.apple = Apple()
    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN and event.key == K_RIGHT:
                    self.snake.direction = 0
                if event.type == KEYDOWN and event.key == K_UP:
                    self.snake.direction = 1
                if event.type == KEYDOWN and event.key == K_DOWN:
                    self.snake.direction = 2
                if event.type == KEYDOWN and event.key == K_LEFT:
                    self.snake.direction = 3


class Snake:
    def __init__(self):
        self.direction = 0
        self.x = 40
        self.y = 40
        self.length = 3

    def move(self):
        if self.direction == 0:  # Right
            pygame.draw.rect(screen, SNAKE_COLOR, pygame.Rect(self.x+10, self.y+10, 10, 10))
            pygame.display.flip()
        if self.direction == 1:  # Up
            pygame.draw.rect(screen, SNAKE_COLOR, pygame.Rect(self.x, self.y-10, 10, 10))
            pygame.display.flip()
        if self.direction == 2:  # Down
            pygame.draw.rect(screen, SNAKE_COLOR, pygame.Rect(self.x, self.y+10, 10, 10))
            pygame.display.flip()
        if self.direction == 3:  # Left
            pygame.draw.rect(screen, SNAKE_COLOR, pygame.Rect(self.x-10, self.y, 10, 10))
            pygame.display.flip()


class Apple:
    def __init__(self):
        while True:
            self.x = random.randrange(0, 510, 10)
            self.y = random.randrange(0, 510, 10)
            self.position = (self.x, self.y)
            if self.position in taken_spaces:
                continue
            else:
                break

    def spawn(self):
        pygame.draw.rect(screen, APPLE_COLOR, pygame.Rect(self.x, self.y, 10, 10))
        pygame.display.flip()









# THE END
