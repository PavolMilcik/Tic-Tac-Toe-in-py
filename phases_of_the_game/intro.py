from other_constants import SEPARATOR
import phase_constatns as phase_const
from time import sleep


def intro_print():
    print("\n\n\tINTRO: Tic-Tac-Toe game.\n" + SEPARATOR + "\nStep into the world of tic-tac-toe,\nwhere two rival players will engage in a battle of wits,\nand the outcome will either crown a triumphant winner or leave the game hanging in an exciting draw.")
    sleep(1)
    return phase_const.MAIN_MENU_PHASE
