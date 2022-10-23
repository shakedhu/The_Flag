import Screen
import consts
import pygame
import sys

def night_screen():
    WHITE = (200, 200, 200)
    Screen.screen.fill(consts.SCREEN_MINE_COLOR)

    def drawGrid():
        blockSize = 20  # Set the size of the grid block
        for x in range(0, consts.WINDOW_WIDTH, blockSize):
            for y in range(0, consts.WINDOW_HEIGHT, blockSize):
                rect = pygame.Rect(x, y, blockSize, blockSize)
                pygame.draw.rect(Screen.screen, WHITE, rect, 1)

    while True:
        drawGrid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

night_screen()