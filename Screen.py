import consts
import pygame
import random
import sys

# board_game = []
# for row in range(consts.ROWS):
#     for col in range(consts.COLS):
#         board_game.append([row, col])
# print(board_game)

#caption
pygame.display.set_caption('flag_game')



screen = pygame.display.set_mode(
        (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
screen.fill(consts.SCREEN_NORMAL_COLOR)
pygame.display.flip()

def green_screen():
    pygame.init()
    imp = pygame.image.load("grass.png").convert()

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
    # pygame.quit()

# green_screen()


def night_screen():
    BLACK = (0, 0, 0)
    WHITE = (200, 200, 200)
    screen.fill(BLACK)

    def drawGrid():
        blockSize = 400  # Set the size of the grid block
        for x in range(0, consts.WINDOW_WIDTH, blockSize):
            for y in range(0, consts.WINDOW_HEIGHT, blockSize):
                rect = pygame.Rect(x, y, blockSize, blockSize)
                pygame.draw.rect(screen, WHITE, rect, 1)

    while True:
        drawGrid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


    

