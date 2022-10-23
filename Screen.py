import consts
import pygame
import random
import sys

game_field = []

screen = pygame.display.set_mode(
    (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
screen.fill(consts.SCREEN_NORMAL_COLOR)
pygame.display.flip()

# caption
pygame.display.set_caption('flag_game')

def create_game_field():
    global game_field
    for i in range(consts.ROWS):
        for j in range(consts.COLS):
            game_field.append(j)


def green_screen():
    pygame.init()
    imp = pygame.image.load("grass.png").convert()

    imp = pygame.transform.scale(imp, (75, 50))
    for i in range(20):
        random_num_width = random.randint(0, consts.WINDOW_WIDTH - 75)
        random_num_height = random.randint(0, consts.WINDOW_HEIGHT - 50)

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
    # pygame.quit()
green_screen()



def draw_message(message, font_size, color, location):
    font = pygame.font.SysFont(consts.WIN_FONT, font_size)
    text_img = font.render(message, True, color)
    screen.blit(text_img, location)


def draw_welcome():
    draw_message(consts.START_MESSAGE, consts.START_MESSAGE_SIZE, consts.WHITE,
                 consts.START_MESSAGE_LOCATION)
def draw_lose_message():
    draw_message(consts.LOSE_MESSAGE, consts.LOSE_FONT_SIZE,
                 consts.WHITE, consts.LOSE_LOCATION)


def draw_win_message():
    draw_message(consts.WIN_MESSAGE, consts.WIN_FONT_SIZE,
                 consts.WHITE, consts.WIN_LOCATION)



#
# def draw_game():
#     # draw_game()


# draw_game()