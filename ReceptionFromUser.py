import turtle
from sys import exit
import pygame
import consts
import keyboard
import Screen

def stop():
    turtle.bye()
    exit()

def move_player():
    global current_player_location
    for i in Screen.create_game_field():
        for j in Screen.create_game_field():
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if pygame.key.get_pressed() == pygame.K_UP:
                        if Screen.create_game_field()[i] != 0:
                            Screen.create_game_field()[i] += 1
                            current_player_location = [current_player_location[i], current_player_location[j]]
                            consts.GREEN_SCREEN.blit(consts.NORMAL_SOLDIER_IMG, current_player_location)

                    elif pygame.key.get_pressed() == pygame.K_DOWN:
                        if Screen.create_game_field()[i] != 25:
                            Screen.create_game_field()[i] -= 1
                            current_player_location = [Screen.create_game_field()[i], Screen.create_game_field()[j]]
                            consts.GREEN_SCREEN.blit(consts.NORMAL_SOLDIER_IMG, current_player_location)

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

def should_show_mine_field():
    while True:
        if keyboard.read_key() == pygame.K_ENTER:
            return True

        return False
