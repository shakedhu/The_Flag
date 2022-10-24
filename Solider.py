import ReceptionFromUser
import consts
import pygame
import MineField


def create_start_soldier():
    soldier = pygame.transform.scale(consts.NORMAL_SOLDIER_IMG, (consts.START_PLAYER_WIDTH, consts.START_PLAYER_HEIGHT))
    consts.SCREEN.blit(soldier, consts.START_PLAYER_POSITION)

def index_upper_body():
    location_solider = ReceptionFromUser.move_player()
    list_upper = []
    x = location_solider[0]
    y = location_solider[1]
    for i in range(3):
        for j in range(2):
            location_solider = [x + (i * 20), y + (j * 20)]
            list_upper.append(location_solider)
    return list_upper

def index_legs():
    location_solider = ReceptionFromUser.move_player()
    list_legs = []
    x = location_solider[0]
    y = location_solider[1]
    for i in range(1):
        for j in range(2):
            location_solider = [x + (i * 20) + 60, y + (j * 20)]
            list_legs.append(location_solider)
    return list_legs


def is_touching_flag():
    upper_part_location = index_upper_body()
    for i in range(len(upper_part_location)):
        for j in range(2):
            if j == consts.FLAG_LOCATION:
                return True

    return False


def is_touching_mine():
    list_of_mines_locations = MineField.list_location_mines
    legs_location = index_legs()
    for i in range(consts.MINE_NUM):
        for mine in list_of_mines_locations:
            for leg in legs_location:
                if leg == mine:
                    return True

    return False
