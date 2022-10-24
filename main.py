import ReceptionFromUser
import MineField
import Screen


Screen.green_screen()
if ReceptionFromUser.should_show_mine_field():
    MineField.night_screen()
