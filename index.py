import pygame
from sys import exit
from random import randint


def displayScore():
    current_time = int(pygame.time.get_ticks() / 1000) - start_game
    score_surface = test_font.render(
        f'Score: {current_time}', False, (64, 64, 64))
    score_retangulo = score_surface.get_rect(center=(400, 50))
    screen.blit(score_surface, score_retangulo)
    return current_time


def obstacleMovement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5

            if obstacle_rect.bottom == 300:
                screen.blit(snail_surface, obstacle_rect)
            else:
                screen.blit(fly_surface, obstacle_rect)

        obstacle_list = [
            obstacle for obstacle in obstacle_list if obstacle.x > -100]

        return obstacle_list
    else:
        return []


def collisions(player, obstacles):
    if obstacles:
        for obstacles_rect in obstacles:
            if player.colliderect(obstacles_rect):
                return False
    return True


def player_animation():
    # play walking animation if the player is on floor
    # display the jump surface when player is not on floor
    global player_surface, player_index

    if player_retangulo.bottom < 300:
        player_surface = player_jump
    else:
        player_index += 0.1
        if player_index >= len(player_walk):
            player_index = 0
        player_surface = player_walk[int(player_index)]


pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('O Corredor')
clock = pygame.time.Clock()
test_font = pygame.font.Font('UltimatePygameIntro/font/Pixeltype.ttf', 40)
game_active = False
start_game = 0
score = 0

sky_surface = pygame.image.load(
    'UltimatePygameIntro/graphics/Sky.png').convert()
ground_surface = pygame.image.load(
    'UltimatePygameIntro/graphics/ground.png').convert()


# score_surface = test_font.render('Bem Vindo ao Corredor', False, (64, 64, 64))
# score_retangulo = score_surface.get_rect(center=(400, 50))


# Obstacles
snail_surface = pygame.image.load(
    'UltimatePygameIntro/graphics/snail/snail1.png').convert_alpha()
fly_surface = pygame.image.load(
    'UltimatePygameIntro/graphics/Fly/Fly1.png').convert_alpha()


obstacle_rect_list = []

player_walk_1 = pygame.image.load(
    'UltimatePygameIntro/graphics/Player/player_walk_1.png').convert_alpha()
player_walk_2 = pygame.image.load(
    'UltimatePygameIntro/graphics/Player/player_walk_2.png').convert_alpha()
player_walk = [player_walk_1, player_walk_2]
player_index = 0
player_jump = pygame.image.load(
    'UltimatePygameIntro/graphics/Player/jump.png').convert_alpha()

player_surface = player_walk[player_index]
player_retangulo = player_surface.get_rect(midbottom=(80, 300))
player_gravidade = 0


# Intro Screen

player_stand = pygame.image.load(
    'UltimatePygameIntro/graphics/Player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center=(400, 200))


game_name = test_font.render('Pixel Runner', False, (111, 196, 169))
game_name_retangulo = game_name.get_rect(center=(400, 80))

game_message = test_font.render('Press Space to RUN', False, (111, 196, 169))
game_message_rect = game_message.get_rect(center=(400, 320))

# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1400)

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
                start_game = int(pygame.time.get_ticks() / 1000)

        if event.type == obstacle_timer and game_active:
            if randint(0, 2):
                obstacle_rect_list.append(
                    snail_surface.get_rect(bottomright=(randint(900, 1100), 300)))
            else:
                obstacle_rect_list.append(
                    fly_surface.get_rect(bottomright=(randint(900, 1100), 210)))

    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        # pygame.draw.rect(screen, '#c0e8ec', score_retangulo)
        # pygame.draw.rect(screen, '#c0e8ec', score_retangulo, 10)
        # screen.blit(score_surface, score_retangulo)
        score = displayScore()

       # snail_retangulo.x -= 4
       # if snail_retangulo.right <= 0:
       #     snail_retangulo.left = 800
       # screen.blit(snail_surface, snail_retangulo)

        # Player
        player_gravidade += 1
        player_retangulo.y += player_gravidade
        if player_retangulo.bottom >= 300:
            player_retangulo.bottom = 300
            player_animation()
        screen.blit(player_surface, player_retangulo)

        # Obstacle Movement
        obstacle_rect_list = obstacleMovement(obstacle_rect_list)

        # Colisão
        game_active = collisions(player_retangulo, obstacle_rect_list)

    else:
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rect)
        obstacle_rect_list.clear()
        player_retangulo.midbottom = (80, 300)
        player_gravidade = 0

        score_message = test_font.render(
            f'Seu score: {score} pontos', False, (111, 196, 169))
        score_message_rect = score_message.get_rect(center=(400, 330))
        screen.blit(game_name, game_name_retangulo)

        if score == 0:
            screen.blit(game_message, game_message_rect)
        else:
            screen.blit(score_message, score_message_rect)
    pygame.display.update()
    clock.tick(60)
