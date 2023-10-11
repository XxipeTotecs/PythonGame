import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('O Corredor')
clock = pygame.time.Clock()
test_font = pygame.font.Font('UltimatePygameIntro/font/Pixeltype.ttf', 40)

sky_surface = pygame.image.load(
    'UltimatePygameIntro/graphics/Sky.png').convert()
ground_surface = pygame.image.load(
    'UltimatePygameIntro/graphics/ground.png').convert()
text_surface = test_font.render('Bem Vindo ao Corredor', False, 'Black')

snail_surface = pygame.image.load(
    'UltimatePygameIntro/graphics/snail/snail1.png').convert_alpha()
snail_retangulo = snail_surface.get_rect(midbottom=(80, 300))

player_surface = pygame.image.load(
    'UltimatePygameIntro/graphics/Player/player_walk_1.png').convert_alpha()
player_retangulo = player_surface.get_rect(midbottom=(80, 300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # escrever todos nossos elementos
    # dar update em tudo
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (250, 50))

    snail_retangulo.x -= 4
    if snail_retangulo.right <= 0:
        snail_retangulo.left = 800
    screen.blit(snail_surface, snail_retangulo)
    screen.blit(player_surface, player_retangulo)

    pygame.display.update()
    clock.tick(60)
