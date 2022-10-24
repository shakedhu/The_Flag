import turtle
from sys import exit
import pygame

import MineField
import Screen
import consts

# def stop():
#     turtle.bye()
#     exit()
#
# def move_player():
#     current_player_location = consts.START_PLAYER_POSITION
#     for event in pygame.event.get():
#     # if current_player_location[0] < 0 or current_player_location[1] < 0:
#
#         if event.type == pygame.K_UP:
#             current_player_location[0] += 20
#         elif event.type == pygame.K_DOWN:
#             if current_player_location[0] != 0:
#                 current_player_location[0] -= 20
#         if event.type == pygame.K_RIGHT:
#             current_player_location[1] += 20
#         elif event.type == pygame.K_LEFT:
#             current_player_location[1] -= 20
#
# def should_show_mine_field():
#     for event in pygame.event.get():
#         if event.type == pygame.K_KP_ENTER:
#             return True
#
#         return False





def move_player():
    pygame.init()
    velocity = 20
    current_player_location = consts.START_PLAYER_POSITION

    # Creating an Infinite loop
    run = True
    while run:


        for event in pygame.event.get():

            # Closing the window and program if the
            # type of the event is QUIT
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

            # Checking event key if the type
            # of the event is KEYDOWN i.e.
            # keyboard button is pressed
            if event.type == pygame.KEYDOWN:

                # Decreasing the x coordinate
                # if the button pressed is
                # Left arrow key
                if event.key == pygame.K_LEFT:
                    current_player_location[1] -= velocity

                # Increasing the x coordinate
                # if the button pressed is
                # Right arrow key
                if event.key == pygame.K_RIGHT:
                    current_player_location[1] += velocity

                # Decreasing the y coordinate
                # if the button pressed is
                # Up arrow key
                if event.key == pygame.K_UP:
                    current_player_location[0] -= velocity

                # Increasing the y coordinate
                # if the button pressed is
                # Down arrow key
                if event.key == pygame.K_DOWN:
                    current_player_location[0] += velocity

            # Draws the surface object to the screen.
            pygame.display.update()