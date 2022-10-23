import consts
def is_touching_flag(upper_part_location):
    for i in range(len(upper_part_location)):
        for j in range(2):
            if j == consts.FLAG_LOCATION:
                return True

    return False

def is_touching_mine(upper_part_location, list_of_mines_locations):
    for i in range(consts.MINE_NUM):
        for location in range(len(list_of_mines_locations)):
            place = upper_part_location[1][1][1] + 2  # פלוס 2 כדי שיגיע לרגליים.
            if place + 40 == location:  # מפלוס 2 בגלל הרוחב של הגוף שלו. (באינדקסים זה 40). .
                return True

    return False