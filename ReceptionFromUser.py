import turtle
from sys import exit
import pygame
import consts

def stop():
    turtle.bye()
    exit()

def move_player():
    current_player_location = consts.START_PLAYER_POSITION
    for event in pygame.event.get():
    # if current_player_location[0] < 0 or current_player_location[1] < 0:

        if event.type == pygame.K_UP:
            current_player_location[0] += 20
        elif event.type == pygame.K_DOWN:
            if current_player_location[0] != 0:
                current_player_location[0] -= 20
        if event.type == pygame.K_RIGHT:
            current_player_location[1] += 20
        elif event.type == pygame.K_LEFT:
            current_player_location[1] -= 20

def should_show_mine_field():
    for event in pygame.event.get():
        if event.type == pygame.K_KP_ENTER:
            return True

        return False
