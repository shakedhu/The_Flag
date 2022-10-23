import turtle
from sys import exit
import pygame

def stop():
    turtle.bye()
    exit()

def move_player(player_x_location, player_y_location):
    for event in pygame.event.get():
        if event.type == pygame.K_UP:
            player_y_location += 1
        elif event.type == pygame.K_DOWN:
            player_y_location -= 1
        elif event.type == pygame.K_RIGHT:
            player_x_location += 1
        elif event.type == pygame.K_LEFT:
            player_x_location -= 1

def should_show_mine_field():
    for event in pygame.event.get():
        if event.type == pygame.K_KP_ENTER:
            return True

        return False
