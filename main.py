from cgitb import text
from turtle import right
import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

score_surf = test_font.render('My game', False, "#ffffff")
score_rect =  score_surf.get_rect(center = (400,50))

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (600, 300))

play_surf = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
play_rect = play_surf.get_rect(midbottom = (80,300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        # if event.type == pygame.MOUSEBUTTONUP:
        #     print(event)

    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0,300))
    pygame.draw.rect(screen, 'Pink', score_rect, border_radius= 10)
    pygame.draw.line(screen, 'Gold', (0,0), (800,400), 10)
    screen.blit(score_surf, score_rect)

    snail_rect.x += -4

    if snail_rect.right <= 0: snail_rect.left = 800
    screen.blit(snail_surface, snail_rect)

    play_rect.left += 1
    screen.blit(play_surf, play_rect)

    # if play_rect.colliderect(snail_rect):
    #     print('col')

    # mouse_pos = pygame.mouse.get_pos()
    # if play_rect.collidepoint(mouse_pos):
    #     print(pygame.mouse.get_pressed())

    pygame.display.update()
    clock.tick(60)



