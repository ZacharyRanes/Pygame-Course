import pygame
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((800, 700), 0, 32)

sprite1 = pygame.image.load('images/butterfly.png')
sprite1 = pygame.transform.scale(sprite1, (60, 60))
sprite1_width = sprite1.get_width()
sprite1_height = sprite1.get_height()

pygame.display.set_caption("Hello Mouse")
screen.fill((0, 0, 0))

game_over = False
sprite1_x_pos, sprite1_y_pos = (0, 0)

while not game_over:

    delta_time = clock.tick(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.MOUSEMOTION:
            sprite1_x_pos, sprite1_y_pos = event.pos
            sprite1_x_pos -= sprite1_width / 2
            sprite1_y_pos -= sprite1_height / 2

    pressed = pygame.key.get_pressed()
    if pressed[K_UP]:
        sprite1_y_pos -= 0.5 * delta_time
    if pressed[K_DOWN]:
        sprite1_y_pos += 0.5 * delta_time
    if pressed[K_LEFT]:
        sprite1_x_pos -= 0.5 * delta_time
    if pressed[K_RIGHT]:
        sprite1_x_pos += 0.5 * delta_time
    if pressed[K_SPACE]:
        sprite1_x_pos = 0
        sprite1_y_pos = 0

    if sprite1_x_pos > (screen.get_width() - sprite1_width):
        sprite1_x_pos = screen.get_width() - sprite1_width
    if sprite1_x_pos < 0:
        sprite1_x_pos = 0

    if sprite1_y_pos > (screen.get_height() - sprite1_height):
        sprite1_y_pos = screen.get_height() - sprite1_height
    if sprite1_y_pos < 0:
        sprite1_y_pos = 0

    screen.fill((0, 0, 0))
    screen.blit(sprite1, (sprite1_x_pos, sprite1_y_pos))
    pygame.display.update()

pygame.quit()
