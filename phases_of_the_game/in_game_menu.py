import phase_constatns as phase_const
from other_constants import SEPARATOR
import other_constants as oth_const
from time import sleep


def in_game_menu():
    print("\n\n\tGAME MENU\n" + SEPARATOR + "\nYou can choose from the following options --->\n" + SEPARATOR)
    sleep(1)

    menu_list = ["Start a Completely New Game with New Players", "Start Duel and the Battle of wits between " + str(oth_const.FIRST_PLAYER_NAME) + " and " + str(oth_const.SECOND_PLAYER_NAME), "Load Game", "Save Game", "End the Tic-Tac-Toe Game"]
    
    enumerate_menu_dict = dict(enumerate(menu_list, 1))
    for k, v in enumerate_menu_dict.items():
        print(k, " - ", v)
    print("")
    
    while True:
        sleep(1)
        user_menu_selection_input = input("Which option will you choose: ")
        if user_menu_selection_input == "1":
            sleep(1)
            oth_const.FIRST_PLAYER_ALL_WINS = 0
            oth_const.SECOND_PLAYER_ALL_WINS = 0
            return phase_const.NAMES_SYMBOLS_FOR_NEW_GAME_PHASE
        elif user_menu_selection_input == "2":
            sleep(1)
            oth_const.GRID_FIELD_LIST = []
            return phase_const.START_DUEL_PHASE
        elif user_menu_selection_input == "3":
            sleep(1)
            return phase_const.LOAD_GAME_PHASE
        elif user_menu_selection_input == "4":
            sleep(1)
            return phase_const.SAVE_GAME_PHASE
        elif user_menu_selection_input == "5":
            sleep(1)
            return phase_const.END_GAME_PHASE
        else:
            print("Out of range, try again!\n")
            continue
