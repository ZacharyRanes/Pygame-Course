import pygame
pygame.init()

screen = pygame.display.set_mode((800, 700), 0, 32)
sprite1 = pygame.image.load('images/football.png')

pygame.display.set_caption("Hello Sprite")
screen.fill((0, 0, 0))
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    screen.blit(sprite1, (400 - sprite1.get_height() / 2,
                          350 - sprite1.get_width() / 2))
    pygame.display.update()
pygame.quit()
