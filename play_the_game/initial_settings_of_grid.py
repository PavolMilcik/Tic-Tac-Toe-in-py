import phase_constatns as phase_const
from other_constants import SEPARATOR
import other_constants as oth_const
from play_the_game.start_duel import start_duel
from time import sleep


# setting grid
def initial_settings_of_grid():
    sleep(1)
    print("\n\n\tINITIAL SETTINGS BEFORE THE DUEL\n" + SEPARATOR)
    print("But first, choose how the playing field will look.\nThe standard playing field in the tic-tac-toe game looks like this - it consists of 3 rows and 3 columns.")
    
    # standard pattern playing field
    for row in range(3):
        for column in range(3):
            print("_", end=" ")
        print()
    
    sleep(1)    
    print("\nIf you want to keep it and proceed with the game, select option 1.\nIf you want to choose a custom playing field, select option 2.")
    print(SEPARATOR)
    
    print("1 - Start duel with standart grid")
    print("2 - Create a custom playing field")
    while True:
        user_input = input("\nYour choice is: ")
        if user_input == "1":
            oth_const.GRID_FIELD_LIST = []
            oth_const.GRID_ROWS = 3
            oth_const.GRID_COLUMNS = 3
            sleep(1)
            start_duel()
            return phase_const.AFTER_DUEL_PHASE
        elif user_input == "2":
            sleep(1)
            return create_grid_by_players()
        else:
            print("\nOut of range, try again!")
            continue



def create_grid_by_players():
    print("\n\nYou've chosen to design your own grid - your own playing field.")
    print("\n\n\tCREATE YOUR OWN GAME GRID")
    print(SEPARATOR)
    print("All right, let's begin with the number of rows, and then the number of columns.")
    print("For the gaming experience, we recommend staying within the range of 3 to 5 rows, and the same goes for columns.")
    print(SEPARATOR)
    print("!The number of rows and columns must be the same!")
    print(SEPARATOR)
    
    while True:
        while True:
            user_rows_input = input("Number of rows: ")
            try:
                user_rows_input = int(user_rows_input)
            except ValueError:
                print("\nPlease write only integers. Thanks.")
                continue
            if user_rows_input < 3 or user_rows_input > 5:
                print("\nRows are out of range, try again!")
                continue
            else:
                print("You have chosen this number of rows: " + str(user_rows_input) + "\n")
                break 
                
        while True:
            user_columns_input = input("Number of columns: ")
            try:
                user_columns_input = int(user_columns_input)
            except ValueError:
                print("\nPlease write only integers. Thanks.")
                continue
            if user_columns_input < 3 or user_columns_input > 5:
                print("\nColumns are out of range, try again!")
                continue
            else:
                print("You have chosen this number of columns: " + str(user_columns_input))
                break
    
        if user_rows_input != user_columns_input:
            print("\nThe number of rows and columns must be the same!\n")
            continue
        else:
            break
    
    # players created playing field
    for row in range(user_rows_input):
        for column in range(user_columns_input):
            print("_", end=" ")
        print()
    return confirm_grid(user_rows_input, user_columns_input)


def confirm_grid(user_rows_input, user_columns_input):
    
    print("\nConfirm the playing field you've created, or start over.")
    
    print("1 - Confirm grid")
    print("2 - Start over")
    while True:
        user_input = input("\nYour choice is: ")
        if user_input == "1":
            oth_const.GRID_ROWS = user_rows_input
            oth_const.GRID_COLUMNS = user_columns_input
            oth_const.GRID_FIELD_LIST = []
            sleep(1)
            start_duel()
            return phase_const.AFTER_DUEL_PHASE
        elif user_input == "2":
            sleep(1)
            return create_grid_by_players()
        else:
            print("\nOut of range, try again!")
            continue
