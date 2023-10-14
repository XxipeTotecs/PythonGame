import pygame
from sys import exit


def displayScore():
    current_time = int(pygame.time.get_ticks() / 1000) - start_game
    score_surface = test_font.render(
        f'Score: {current_time}', False, (64, 64, 64))
    score_retangulo = score_surface.get_rect(center=(400, 50))
    screen.blit(score_surface, score_retangulo)


pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('O Corredor')
clock = pygame.time.Clock()
test_font = pygame.font.Font('UltimatePygameIntro/font/Pixeltype.ttf', 40)
game_active = False
start_game = 0

sky_surface = pygame.image.load(
    'UltimatePygameIntro/graphics/Sky.png').convert()
ground_surface = pygame.image.load(
    'UltimatePygameIntro/graphics/ground.png').convert()


# score_surface = test_font.render('Bem Vindo ao Corredor', False, (64, 64, 64))
# score_retangulo = score_surface.get_rect(center=(400, 50))

snail_surface = pygame.image.load(
    'UltimatePygameIntro/graphics/snail/snail1.png').convert_alpha()
snail_retangulo = snail_surface.get_rect(midbottom=(80, 300))

player_surface = pygame.image.load(
    'UltimatePygameIntro/graphics/Player/player_walk_1.png').convert_alpha()
player_retangulo = player_surface.get_rect(midbottom=(80, 300))
player_gravidade = 0


# Intro Screen

player_stand = pygame.image.load(
    'UltimatePygameIntro/graphics/Player/player_stand.png')
player_stand_rect = player_stand.get_rect(center=(400, 200))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_retangulo.collidepoint(event.pos) and player_retangulo.bottom >= 300:
                    player_gravidade = -20

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_retangulo.bottom >= 300:
                    player_gravidade = -20

        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_retangulo.left = 800
                start_game = int(pygame.time.get_ticks() / 1000)

    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        # pygame.draw.rect(screen, '#c0e8ec', score_retangulo)
        # pygame.draw.rect(screen, '#c0e8ec', score_retangulo, 10)
        # screen.blit(score_surface, score_retangulo)
        displayScore()

        snail_retangulo.x -= 4
        if snail_retangulo.right <= 0:
            snail_retangulo.left = 800
        screen.blit(snail_surface, snail_retangulo)

        # Player
        player_gravidade += 1
        player_retangulo.y += player_gravidade
        if player_retangulo.bottom >= 300:
            player_retangulo.bottom = 300
        screen.blit(player_surface, player_retangulo)

        # Colisão
        if snail_retangulo.colliderect(player_retangulo):
            game_active = False

    else:
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rect)

    pygame.display.update()
    clock.tick(60)
