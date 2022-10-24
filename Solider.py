import consts
import pygame

def create_start_soldier():
    soldier = pygame.transform.scale(consts.NORMAL_SOLDIER_IMG,(consts.START_PLAYER_WIDTH,consts.START_PLAYER_HEIGHT))
    consts.SCREEN.blit(soldier, consts.START_PLAYER_POSITION)

# def location_soldier():


# def index_upper_body():
#     location_solider = [0, 0]
#     list_upper = []
#     x = location_solider[0]
#     y = location_solider[1]
#     for i in range(3):
#         for j in range(2):
#             location_solider = [x+i, y+j]
#             list_upper.append(location_solider)
#     print(list_upper)

# index_upper_body()
#
#
# def index_legs(location_solider):
#     # location_solider = [0, 0]
#     list_legs = []
#     x = location_solider[0]
#     y = location_solider[1]
#     for i in range(1):
#         for j in range(2):
#             location_solider = [x+i+3, y+j]
#             list_legs.append(location_solider)
#     print(list_legs)
# index_legs()

# def is_touching_flag(upper_part_location):
#     for i in range(len(upper_part_location)):
#         for j in range(2):
#             if j == consts.FLAG_LOCATION:
#                 return True
#
#     return False
#
# def is_touching_mine(upper_part_location, list_of_mines_locations):
#     for i in range(consts.MINE_NUM):
#         for location in range(len(list_of_mines_locations)):
#             place = upper_part_location[1][1][1] + 2  # פלוס 2 כדי שיגיע לרגליים.
#             if place + 40 == location:  # מפלוס 2 בגלל הרוחב של הגוף שלו. (באינדקסים זה 40). .
#                 return True
#
#     return False