import pygame

ROWS = 25
COLS = 50
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 500
SCREEN_NORMAL_COLOR = (69, 139, 0)
SCREEN_MINE_COLOR = (3, 3, 3)
MINE_LINES_COLOR = (69, 139, 0)
WHITE = (248, 248, 255)
SCREEN = pygame.display.set_mode(
    (WINDOW_WIDTH, WINDOW_HEIGHT))
START_MESSAGE = "Welcome to The Flag game. " \
                "Have Fun!"
START_MESSAGE_SIZE = 20
START_MESSAGE_LOCATION = (60, 0)

MINE_NUM = 20

FLAG_IMG = pygame.image.load("flag.png")
FLAG_IMG = pygame.transform.scale(FLAG_IMG, (75, 50))
NORMAL_SOLDIER_IMG = pygame.image.load("soldier.png")
SOLDIER_NIGHT_IMG = pygame.image.load("soldier_nigth.png")
INJURY_IMG = pygame.image.load("injury.png")
MINE_IMG = pygame.image.load("mine.png")
GRASS_IMG = pygame.image.load("grass.png")
EXPLOTION_IMG = pygame.image.load("explotion.png")

FLAG_HEIGHT = 440
FLAG_WIDTH = 920
FLAG_X = WINDOW_WIDTH / 2 - (FLAG_WIDTH / 2)
FLAG_Y = WINDOW_HEIGHT * 0.8
FLAG_LOCATION = [FLAG_X, FLAG_Y]
FLAG_MIDBOTTOM_X = FLAG_X + FLAG_WIDTH / 2
FLAG_MIDBOTTOM_Y = FLAG_Y + FLAG_HEIGHT

START_PLAYER_HEIGHT = 80
START_PLAYER_WIDTH = 40
START_PLAYER_POSITION = [0, 0]

WIN_MESSAGE = "You won!"
WIN_FONT = "Calibri"
WIN_FONT_SIZE = 20
WIN_LOCATION = (0.2 * WINDOW_WIDTH, WINDOW_HEIGHT / 2 - (WIN_FONT_SIZE / 2))

LOSE_MESSAGE = "You lost!"
LOSE_FONT = "Calibri"
LOSE_FONT_SIZE = 20
LOSE_LOCATION = (0.2 * WINDOW_WIDTH, WINDOW_HEIGHT / 2 - (LOSE_FONT_SIZE / 2))