import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Breakin' Bricks")

bat = pygame.image.load('sprites/paddle.png')
bat = bat.convert_alpha()
bat_rec = bat.get_rect()

ball = pygame.image.load('sprites/football.png')
ball = ball.convert_alpha()
ball_rec = ball.get_rect()

brick = pygame.image.load('sprites/brick.png')
brick = brick.convert_alpha()
brick_rec = brick.get_rect()

clock = pygame.time.Clock()
game_over = False

while not game_over:
    delta_time = clock.tick(50)
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

pygame.quit()
