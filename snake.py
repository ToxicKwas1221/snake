import pygame
from pygame.locals import *
import random
from enum import Enum

# Settings
CAPTION = "Snake"  # Title of the window
SNAKE_COLOR = (0, 255, 0)  # RGB
BACKGROUND_COLOR = (53, 53, 53)  # RGB
APPLE_COLOR = (255, 0, 0)  # RGB
WIDTH = 700
HEIGHT = 700
DELAY = 20
WALL_HIT = False


class Direction(Enum):
    RIGHT = 0
    UP = 1
    DOWN = 2
    LEFT = 3


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
                    print("Your score is {}.".format(self.score))
                    pygame.quit()
                    exit()
                """0-right 1-up 2-down 3-left"""
                if event.type == KEYDOWN:
                    if event.key == K_RIGHT:
                        if self.snake.direction == Direction.LEFT:  # IOW: if snake is not going in opposite direction
                            pass
                        else:
                            self.snake.direction = Direction.RIGHT
                            self.tick()
                        while not pygame.event.peek(KEYDOWN):  # IOW: while no buttons pressed
                            self.tick()

                    elif event.key == K_UP:
                        if self.snake.direction == Direction.DOWN:
                            pass
                        else:
                            self.snake.direction = Direction.UP
                            self.tick()
                        while not pygame.event.peek(KEYDOWN):
                            self.tick()

                    elif event.key == K_DOWN:
                        if self.snake.direction == Direction.UP:
                            pass
                        else:
                            self.snake.direction = Direction.DOWN
                            self.tick()
                        while not pygame.event.peek(KEYDOWN):
                            self.tick()

                    elif event.key == K_LEFT:
                        if self.snake.direction == Direction.RIGHT:
                            pass
                        else:
                            self.snake.direction = Direction.LEFT
                            self.tick()
                        while not pygame.event.peek(KEYDOWN):
                            self.tick()

    def end(self):
        print("Your score is {}.".format(self.score))
        pygame.event.set_blocked(None)
        pygame.event.set_allowed(QUIT)
        font = pygame.font.Font(None, 50).render(f'Your score is {self.score}.', True, APPLE_COLOR)
        self.screen.blit(font, (20, 20))
        pygame.display.flip()
        while not pygame.event.peek(QUIT):
            pass
        pygame.quit()
        exit()

    def food_eaten(self):
        if self.snake.head == self.apple.position:
            return True
        else:
            return False

    def body_hit(self):
        return self.snake.head in self.snake.body

    def wall_hit(self):
        if self.snake.head["x"] == WIDTH or self.snake.head["x"] == -10:  # right and left edges
            return True
        elif self.snake.head["y"] == HEIGHT or self.snake.head["y"] == -10:  # down and upper edges
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
        if self.wall_hit():
            if WALL_HIT:
                self.end()
            if self.snake.head['x'] == WIDTH:
                self.snake.head['x'] = 0
            elif self.snake.head['x'] == -10:
                self.snake.head['x'] = WIDTH-10
            elif self.snake.head['y'] == HEIGHT:
                self.snake.head['y'] = 0
            elif self.snake.head['y'] == -10:
                self.snake.head['y'] = HEIGHT-10
        if self.food_eaten():
            self.apple.__init__(self.snake.body, self.snake.head)
            self.score += 1
            self.snake.grow()
            self.show_all()
        if self.body_hit():
            self.end()
        if pygame.event.peek(QUIT):
            print("Your score is {}.".format(self.score))
            pygame.quit()
            exit()


class Snake:
    def __init__(self):
        self.head = {"x": 70, "y": 30}
        self.body = [{"x": 40, "y": 30}, {"x": 50, "y": 30}, {"x": 60, "y": 30}]  # Coordinates of body parts
        self.direction = Direction.RIGHT

    def move(self):
        for num, part in enumerate(self.body):
            try:
                self.body[num] = self.body[num + 1]
            except IndexError:  # Will occur when iteration got to the last body part
                self.body[num] = {"x": self.head["x"], "y": self.head["y"]}

        if self.direction == Direction.RIGHT:
            self.head["x"] += 10
        elif self.direction == Direction.UP:
            self.head["y"] -= 10
        elif self.direction == Direction.DOWN:
            self.head["y"] += 10
        elif self.direction == Direction.LEFT:
            self.head["x"] -= 10

    def show(self, surface):  # Displays the current position of the snake
        pygame.draw.rect(surface, SNAKE_COLOR, pygame.Rect(self.head["x"], self.head["y"], 10, 10))
        for part in self.body:
            pygame.draw.rect(surface, SNAKE_COLOR, pygame.Rect(part['x'], part["y"], 10, 10))

    def grow(self):
        self.body.insert(0, self.body[0])


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