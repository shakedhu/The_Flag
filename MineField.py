# import Screen
import consts
import pygame
import sys
import random

def night_screen():
    screen = pygame.display.set_mode(
        (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
    screen.fill(consts.SCREEN_MINE_COLOR)

    def random_mines():
        pygame.init()
        imp = consts.MINE_IMG.convert()

        imp = pygame.transform.scale(imp, (60, 20))
        for i in range(20):
            random_num_width = random.randint(0, consts.WINDOW_WIDTH - 75)
            random_num_height = random.randint(0, consts.WINDOW_HEIGHT - 50)

            screen.blit(imp, (random_num_width, random_num_height))
    random_mines()
    def drawGrid():
        pygame.init()
        blockSize = 20  # Set the size of the grid block
        for x in range(0, consts.WINDOW_WIDTH, blockSize):
            for y in range(0, consts.WINDOW_HEIGHT, blockSize):
                rect = pygame.Rect(x, y, blockSize, blockSize)
                pygame.draw.rect(screen, consts.MINE_LINES_COLOR, rect, 1)

    while True:
        drawGrid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

night_screen()