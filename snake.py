import pygame
import random
import sys

# Settings
TITLE = "Snake"
SNAKE_COLOR = (200, 0, 0)
BACKGROUD_COLOR = ()


pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption(TITLE)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            pygame.draw.rect(screen, SNAKE_COLOR, pygame.Rect((60, 60, 60, 60)))
            pygame.display.flip()
