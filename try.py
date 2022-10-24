def index_upper_body():
    # location_solider = ReceptionFromUser.move_player()
    location_solider = [0, 0]
    list_upper = []
    x = location_solider[0]
    y = location_solider[1]
    for i in range(3):
        for j in range(2):
            location_solider = [x+(i*20), y+(j*20)]
            list_upper.append(location_solider)
    print(list_upper)

index_upper_body()

def index_legs():
    # location_solider = ReceptionFromUser.move_player()
    location_solider = [0, 0]
    list_legs = []
    x = location_solider[0]
    y = location_solider[1]
    for i in range(1):
        for j in range(2):
            location_solider = [x+(i*20)+60, y+(j*20)]
            list_legs.append(location_solider)
    print(list_legs)
index_legs()