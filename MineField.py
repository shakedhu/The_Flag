# import Screen
import consts
import pygame
import sys
import random
import sys

start_location_solider = [[0, 0], [0, 20], [20, 0], [20, 20], [40, 0], [40, 20]] #המיקומים ההתחלתים של החיילים שלא יכולים להיות בהם מוקשים
mine_field = []

list_location_mines = []
def night_screen():
    consts.SCREEN.fill(consts.SCREEN_MINE_COLOR)
    consts.SCREEN.fill(consts.SCREEN_MINE_COLOR)

    def create_start_night_soldier():
        soldier = pygame.transform.scale(consts.SOLDIER_NIGHT_IMG,
                                         (consts.START_PLAYER_WIDTH, consts.START_PLAYER_HEIGHT))
        consts.SCREEN.blit(soldier, consts.START_PLAYER_POSITION)


    def random_mines():
        pygame.init()
        imp = consts.MINE_IMG.convert()

        imp = pygame.transform.scale(imp, (60, 20))
        for i in range(20):
            random_num_width = random.randint(0, consts.WINDOW_WIDTH - 75)
            random_num_height = random.randint(0, consts.WINDOW_HEIGHT - 50)
            for j in start_location_solider:
                while random_num_width % 20 != 0 or j[0] == random_num_width:
                        random_num_width = random.randint(0, consts.WINDOW_WIDTH - 75)
            for f in start_location_solider:
                while random_num_height % 20 != 0 or f[0] == random_num_height :
                    random_num_height = random.randint(0, consts.WINDOW_HEIGHT - 50)
            list_location_mines.append([random_num_width, random_num_height])
            consts.SCREEN.blit(imp, (random_num_width, random_num_height))

            consts.SCREEN.blit(imp, (random_num_width, random_num_height))
    create_start_night_soldier()
    random_mines()

    def drawGrid():
        pygame.init()
        blockSize = 20  # Set the size of the grid block
        for x in range(0, consts.WINDOW_WIDTH, blockSize):
            for y in range(0, consts.WINDOW_HEIGHT, blockSize):
                rect = pygame.Rect(x, y, blockSize, blockSize)
                pygame.draw.rect(consts.SCREEN, consts.MINE_LINES_COLOR, rect, 1)

    while True:
        drawGrid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

night_screen()