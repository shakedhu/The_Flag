import consts
import pygame
import random
import image

board_game = []
for row in range(consts.ROWS):
    for col in range(consts.COLS):
        board_game.append([row, col])
print(board_game)


#caption
pygame.display.set_caption('flag_game')



screen = pygame.display.set_mode(
        (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
screen.fill(consts.SCREEN_NORMAL_COLOR)
pygame.display.flip()

def green_screen():
    pygame.init()
    imp = pygame.image.load("grass.png").convert_alpha()
    imp.set_colorkey(white)

    imp = pygame.transform.scale(imp, (75, 50))
    for i in range(20):
        random_num_width = random.randint(0, consts.WINDOW_WIDTH-75)
        random_num_height = random.randint(0, consts.WINDOW_HEIGHT-50)

        screen.blit(imp, (random_num_width, random_num_height))

    # paint screen one time
    pygame.display.flip()
    status = True
    while (status):

        # iterate over the list of Event objects
        # that was returned by pygame.event.get() method.
        for i in pygame.event.get():

            # if event object type is QUIT
            # then quitting the pygame
            # and program both.
            if i.type == pygame.QUIT:
                status = False

    # deactivates the pygame library
    pygame.quit()

green_screen()


#random.randint(0, 9)

# def draw_lose_message():
#     draw_message(consts.LOSE_MESSAGE, consts.LOSE_FONT_SIZE,
#                  consts.LOSE_COLOR, consts.LOSE_LOCATION)
#
#
# def draw_win_message():
#     draw_message(consts.WIN_MESSAGE, consts.WIN_FONT_SIZE,
#                  consts.WIN_COLOR, consts.WIN_LOCATION)
#
#
# def draw_message(message, font_size, color, location):
#     font = pygame.font.SysFont(consts.FONT_NAME, font_size)
#     text_img = font.render(message, True, color)
#     screen.blit(text_img, location)


# def draw_game(game_state):
#     screen.fill(consts.BACKGROUND_COLOR)
#     draw_arrow(game_state["rotated_arrow"])
#
#     if game_state["is_bubble_fired"]:
#         draw_bubble(game_state["bullet_bubble"])
#
#     BubblesGrid.draw()
#     draw_border()
#     draw_turns(game_state["turns_left_to_add_row"])
#     Stack.draw()

    # if len(game_state["bubbles_popping"]):
    #     BubblesGrid.animate_bubbles_pop(game_state["bubbles_popping"])
    #     draw_bubbles_popping(game_state["bubbles_popping"])
    #
    # elif game_state["state"] == consts.LOSE_STATE:
    #     draw_lose_message()
    #
    # elif game_state["state"] == consts.WIN_STATE:
    #     draw_win_message()
    #
    # pygame.display.flip()