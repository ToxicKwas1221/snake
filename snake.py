import pygame
from pygame.locals import *
import random
import sys


# Settings
CAPTION = "Snake"
SNAKE_COLOR = (0, 255, 0)
BACKGROUD_COLOR = (53, 53, 53)
APPLE_COLOR = (255, 0, 0)
WIDTH = 500  # Only put number divisible by 10
HEIGHT = 500  # Only put number divisible by 10




class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(CAPTION)
        self.snake = Snake()
        self.apple = Apple(self.snake.body, self.snake.head)

    def start(self):
        self.show_all()
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN and event.key == K_RIGHT:
                    self.snake.direction = 0
                    self.snake.move()
                    self.show_all()
                if event.type == KEYDOWN and event.key == K_UP:
                    self.snake.direction = 1
                    self.snake.move()
                    self.show_all()
                if event.type == KEYDOWN and event.key == K_DOWN:
                    self.snake.direction = 2
                    self.snake.move()
                    self.show_all()
                if event.type == KEYDOWN and event.key == K_LEFT:
                    self.snake.direction = 3
                    self.snake.move()
                    self.show_all()

    def food_eaten(self):
        if self.snake.head == self.apple.position:
            return True
        else:
            return False

    def show_all(self):
        self.screen.fill(BACKGROUD_COLOR)
        self.snake.show(self.screen)
        self.apple.show(self.screen)
        pygame.display.flip()

    def tick(self):
        pass


class Snake:
    def __init__(self):
        self.head = {"x": 70, "y": 30}
        self.tail = {"x": 40, "y": 30}
        self.body = [self.tail, {"x": 50, "y": 30}, {"x": 60, "y": 30}]  # Coordinates of body parts
        self.direction = None

    def move(self):
        """Right FIXME"""
        if self.direction == 0:
            for num, part in enumerate(self.body):  # FIXME
                try:
                    self.body[num] = self.body[num+1]
                except IndexError:  # Will occur when iteration got to the last body part
                    self.body[num] = self.head
            self.tail = self.body[0]
            self.head["x"] += 10
        """Up"""
        if self.direction == 1:
            self.tail = self.body[0]
            for num, part in enumerate(self.body):  # FIXME
                try:
                    self.body[num] = self.body[num + 1]
                except IndexError:  # Will occur when iteration got to the last body part
                    self.body[num] = self.head
            self.head["y"] -= 10

        """Down"""
        if self.direction == 2:
            self.tail = self.body[0]
            for num, part in enumerate(self.body):  # FIXME
                try:
                    self.body[num] = self.body[num + 1]
                except IndexError:  # Will occur when iteration got to the last body part
                    self.body[num] = self.head
            self.head["y"] += 10

        """Left"""
        if self.direction == 3:
            self.tail = self.body[0]
            for num, part in enumerate(self.body):  # FIXME
                try:
                    self.body[num] = self.body[num + 1]
                except IndexError:  # Will occur when iteration got to the last body part
                    self.body[num] = self.head
            self.head["x"] -= 10

    def show(self, surface):  # Displays the current position of the snake
        pygame.draw.rect(surface, SNAKE_COLOR, pygame.Rect(self.head["x"], self.head["y"], 10, 10))
        for part in self.body:
            pygame.draw.rect(surface, SNAKE_COLOR, pygame.Rect(part['x'], part["y"], 10, 10))
        print(self.body, "and head is at:", self.head)  # FIXME


class Apple:
    def __init__(self, snake_body, snake_head):  # generates position
        self.x = random.randrange(0, WIDTH+10, 10)
        self.y = random.randrange(0, HEIGHT+10, 10)
        self.position = {"x": self.x, "y": self.y}
        while self.position in snake_body or self.position == snake_head:
            self.x = random.randrange(0, 510, 10)
            self.y = random.randrange(0, 510, 10)
            self.position = {"x" : self.x, "y" : self.y}

    def show(self, surface):
        pygame.draw.rect(surface, APPLE_COLOR, pygame.Rect(self.x, self.y, 10, 10))



game = Game()
game.start()



# THE END
