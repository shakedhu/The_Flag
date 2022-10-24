import turtle
from sys import exit
import pygame
import consts
import keyboard


current_player_location = consts.START_PLAYER_POSITION

def stop():
    turtle.bye()
    exit()

def move_player():
    global current_player_location
    if keyboard.is_pressed:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed() == pygame.K_UP:
                    if current_player_location[0] != 0:
                        current_player_location[0] += 20
                        current_player_location = [current_player_location[0], current_player_location[1]]
                        consts.GREEN_SCREEN.blit(consts.NORMAL_SOLDIER_IMG, current_player_location)

                elif pygame.key.get_pressed() == pygame.K_DOWN:
                    if current_player_location[0] != 500:
                        current_player_location[0] -= 20
                        consts.GREEN_SCREEN.blit(consts.NORMAL_SOLDIER_IMG, current_player_location)
                        current_player_location = [current_player_location[0], current_player_location[1]]

                elif event.type == pygame.K_RIGHT:
                    if current_player_location[1] != 1000:
                        current_player_location[1] += 20
                        soldier = pygame.transform.scale(consts.NORMAL_SOLDIER_IMG,
                                                         (current_player_location[0], current_player_location[1]))
                        consts.GREEN_SCREEN.blit(soldier, current_player_location)
                        current_player_location = [current_player_location[0], current_player_location[1]]
                elif event.type == pygame.K_LEFT:
                    if current_player_location[1] != 0:
                        current_player_location[1] -= 20

    return current_player_location

def should_show_mine_field():
    for event in pygame.event.get():
        if event.type == pygame.K_KP_ENTER:
            return True

        return False
