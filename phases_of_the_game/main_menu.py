import phase_constatns as phase_const
from other_constants import SEPARATOR
from time import sleep


def menu_selection():
    print("\n\n\tMAIN MENU\n" + SEPARATOR + "\nYou can choose from the following options --->\n" + SEPARATOR)
    sleep(1)

    menu_list = ["Start a New Game", "Load Game", "End the Tic-Tac-Toe Game"]
    
    enumerate_menu_dict = dict(enumerate(menu_list, 1))
    for k, v in enumerate_menu_dict.items():
        print(k, " - ", v)
    print("")
    
    while True:
        sleep(1)
        user_menu_selection_input = input("Which option will you choose: ")
        if user_menu_selection_input == "1":
            sleep(1)
            return phase_const.NAMES_SYMBOLS_FOR_NEW_GAME_PHASE
        elif user_menu_selection_input == "2":
            sleep(1)
            return phase_const.LOAD_GAME_PHASE
        elif user_menu_selection_input == "3":
            sleep(1)
            return phase_const.END_GAME_PHASE
        else:
            print("Out of range, try again!\n")
            continue
