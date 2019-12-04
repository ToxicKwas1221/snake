import pygame
from pygame.locals import *
import random
import sys


# Settings
CAPTION = "Snake"
SNAKE_COLOR = (0, 255, 0)
BACKGROUD_COLOR = (53, 53, 53)
APPLE_COLOR = (255, 0, 0)


pygame.init()
screen = pygame.display.setmode((500, 500))
pygame.display.set_caption(CAPTION)
class Game:
    def __init__(self):
        self.snake = Snake()
        self.apple = Apple()

    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN and event.key == K_DOWN:
                    self.snake.direction = 2
                    self.snake.move()
    def food_eaten(self):
        if self.snake.head == self.apple.position:
            return True
        else:
            return False


class Snake:
    def __init__(self):
        self.body = [self.tail, {"x" : 50, "y" : 30}, {"x" : 60, "y" : 30}]  # coords of body parts
        self.head = {"x" : 70, "y" : 30}
        self.tail = {"x" : 40, "y" : 30}
        self.direction = None

    def move(self):
        if self.direction == 0:  # Right
            self.head["x"] += 10
            for num, part in enumerate(self.body):  # FIXME
                self.body[num] = self.body[num+1]
            pygame.display.update()
        if self.direction == 1:  # Up

        if self.direction == 2:  # Down

        if self.direction == 3:  # Left


class Apple:
    def __init__(self):  # generates position
        while True:
            self.x = random.randrange(0, 510, 10)
            self.y = random.randrange(0, 510, 10)
            self.position = {"x" : self.x, "y" : self.y}
            if self.position in game.snake.body or self.position == game.snake.head:
                continue
            else:
                break

    def spawn(self):  #
        pass

game = Game()
game.start()
