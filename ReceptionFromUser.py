import turtle
from sys import exit
import pygame
import consts

def stop():
    turtle.bye()
    exit()

def move_player():
    global current_player_location
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if pygame.key.get_pressed() == pygame.K_UP:
                if current_player_location[0] != 0:
                    current_player_location[0] += 20
                    current_player_location = [current_player_location[0], current_player_location[1]]
                    consts.SCREEN.blit(consts.NORMAL_SOLDIER_IMG, current_player_location)

            elif pygame.key.get_pressed() == pygame.K_DOWN:
                if current_player_location[0] != 500:
                    current_player_location[0] -= 20
                    consts.SCREEN.blit(consts.NORMAL_SOLDIER_IMG, current_player_location)
                    current_player_location = [current_player_location[0], current_player_location[1]]

            elif event.type == pygame.K_RIGHT:
                if current_player_location[1] != 1000:
                    current_player_location[1] += 20
                    soldier = pygame.transform.scale(consts.NORMAL_SOLDIER_IMG,
                                                     (current_player_location[0], current_player_location[1]))
                    consts.SCREEN.blit(soldier, current_player_location)
                    current_player_location = [current_player_location[0], current_player_location[1]]
            elif event.type == pygame.K_LEFT:
                if current_player_location[1] != 0:
                    current_player_location[1] -= 20

def should_show_mine_field():
    # FPS = 60
    clock = pygame.time.Clock
    run = True
    while run:
        # clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_SPACE]:
            return True
    keys = pygame.key.get_pressed()
    if keys[pygame.K_KP_ENTER]:
        return True
    else:
        return False




