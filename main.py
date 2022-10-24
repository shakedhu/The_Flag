import Screen
import Solider
import MineField
import consts
import ReceptionFromUser
def main():
    Screen.green_screen()
    ReceptionFromUser.stop()
    ReceptionFromUser.move_player()
    if ReceptionFromUser.should_show_mine_field():
        MineField.night_screen()
    if Solider.is_touching_flag():
        Screen.draw_win_message()
    if Solider.is_touching_mine():
        Screen.draw_lose_message()
