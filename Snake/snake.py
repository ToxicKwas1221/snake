
import pygame
from pygame.locals import *
import random
import sys
from colorama import Fore

# Settings
CAPTION = "Snake"  # Title of the window
SNAKE_COLOR = (0, 255, 0)  # RGB
BACKGROUND_COLOR = (53, 53, 53)  # RGB
APPLE_COLOR = (255, 0, 0)  # RGB
WIDTH = int(input("Width(Only put positive number, divisible by 10): "))  # Only put positive number divisible by 10
HEIGHT = int(input("Height(Only put positive number, divisible by 10): "))  # Only put positive number divisible by 10
DELAY = int(input("Delay(Only put positive number): "))  # Milliseconds


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(CAPTION)
        self.snake = Snake()
        self.apple = Apple(self.snake.body, self.snake.head)
        self.score = 0

    def start(self):
        self.show_all()
        pygame.event.set_blocked(MOUSEMOTION)
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    print(Fore.CYAN+"Your score is {}.".upper().format(self.score))
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_RIGHT:
                        self.snake.direction = 0
                        while not pygame.event.peek(KEYDOWN):  # IOW: while no buttons pressed
                            self.tick()
                    elif event.key == K_UP:
                        self.snake.direction = 1
                        while not pygame.event.peek(KEYDOWN):
                            self.tick()
                    elif event.key == K_DOWN:
                        self.snake.direction = 2
                        while not pygame.event.peek(KEYDOWN):
                            self.tick()
                    elif event.key == K_LEFT:
                        self.snake.direction = 3
                        while not pygame.event.peek(KEYDOWN):
                            self.tick()

    def end(self):
        print(Fore.CYAN + "Your score is {}.".upper().format(self.score))
        pygame.event.set_blocked(None)
        pygame.event.set_allowed(QUIT)
        while not pygame.event.peek(QUIT):
            pass
        pygame.quit()
        sys.exit()

    def food_eaten(self):
        if self.snake.head == self.apple.position:
            return True
        else:
            return False

    def body_hit(self):
        if self.snake.head in self.snake.body:
            return True
        else:
            return False

    def wall_hit(self):
        if self.snake.head["x"] == WIDTH or self.snake.head["y"] == HEIGHT:
            return True
        elif self.snake.head["x"] == -10 or self.snake.head["y"] == -10:
            return True
        else:
            return False

    def show_all(self):
        self.screen.fill(BACKGROUND_COLOR)
        self.apple.show(self.screen)
        self.snake.show(self.screen)
        pygame.display.flip()

    def tick(self):
        pygame.time.delay(DELAY)
        self.snake.move()
        self.show_all()
        if self.food_eaten():
            self.apple.__init__(self.snake.body, self.snake.head)
            self.score += 1
            self.snake.grow()
            self.show_all()
        if self.body_hit() or self.wall_hit():
            self.end()


class Snake:
    def __init__(self):
        self.head = {"x": 70, "y": 30}
        self.tail = {"x": 40, "y": 30}
        self.body = [self.tail, {"x": 50, "y": 30}, {"x": 60, "y": 30}]  # Coordinates of body parts
        self.direction = None

    def move(self):
        """Right"""
        if self.direction == 0:
            for num, part in enumerate(self.body):
                try:
                    self.body[num] = self.body[num + 1]
                except IndexError:  # Will occur when iteration got to the last body part
                    self.body[num] = {"x": self.head["x"], "y": self.head["y"]}
            self.tail = self.body[0]
            self.head["x"] += 10
        """Up"""
        if self.direction == 1:
            self.tail = self.body[0]
            for num, part in enumerate(self.body):
                try:
                    self.body[num] = self.body[num + 1]
                except IndexError:  # Will occur when iteration got to the last body part
                    self.body[num] = {"x": self.head["x"], "y": self.head["y"]}
            self.tail = self.body[0]
            self.head["y"] -= 10
        """Down"""
        if self.direction == 2:
            self.tail = self.body[0]
            for num, part in enumerate(self.body):
                try:
                    self.body[num] = self.body[num + 1]
                except IndexError:  # Will occur when iteration got to the last body part
                    self.body[num] = {"x": self.head["x"], "y": self.head["y"]}
            self.tail = self.body[0]
            self.head["y"] += 10
        """Left"""
        if self.direction == 3:
            self.tail = self.body[0]
            for num, part in enumerate(self.body):
                try:
                    self.body[num] = self.body[num + 1]
                except IndexError:  # Will occur when iteration got to the last body part
                    self.body[num] = {"x": self.head["x"], "y": self.head["y"]}
            self.tail = self.body[0]
            self.head["x"] -= 10

    def show(self, surface):  # Displays the current position of the snake
        pygame.draw.rect(surface, SNAKE_COLOR, pygame.Rect(self.head["x"], self.head["y"], 10, 10))
        for part in self.body:
            pygame.draw.rect(surface, SNAKE_COLOR, pygame.Rect(part['x'], part["y"], 10, 10))

    def grow(self):
        self.body.insert(0, self.tail)


class Apple:
    """Generates the position"""
    def __init__(self, snake_body, snake_head):
        self.x = random.randrange(0, WIDTH, 10)
        self.y = random.randrange(0, HEIGHT, 10)
        self.position = {"x": self.x, "y": self.y}
        while self.position in snake_body or self.position == snake_head:
            self.x = random.randrange(0, WIDTH, 10)
            self.y = random.randrange(0, HEIGHT, 10)
            self.position = {"x": self.x, "y": self.y}

    def show(self, surface):
        pygame.draw.rect(surface, APPLE_COLOR, pygame.Rect(self.x, self.y, 10, 10))


if __name__ == '__main__':
    game = Game()
    game.start()

# THE END