import other_constants as oth_const
from play_the_game import grid_field
from time import sleep


def playing_the_game():
    
    # the number of options to input/insert symbols
    number_of_options = oth_const.GRID_ROWS * oth_const.GRID_COLUMNS
    while number_of_options > 0:
        
        sleep(1) 
        # first players input/insert symbol
        print("---- " + str(oth_const.FIRST_PLAYER_NAME) + " as a player number one chooses a position for their '" + str(oth_const.FIRST_PLAYER_SYMBOL) + "' symbol --->")
        while True:
            first_player_row_input = input("Please select a ROW position number: ")
            first_player_column_input = input("Please select a COLUMN position number: ")
            try:
                first_player_row_input = int(first_player_row_input)
                first_player_column_input = int(first_player_column_input)
            except ValueError:
                print("\nPlease write only integers. Thanks.")
                continue
            if first_player_row_input < 1 or first_player_row_input > oth_const.GRID_ROWS:
                print("\nRow is out of range, try again!")
                continue
            elif first_player_column_input < 1 or first_player_column_input > oth_const.GRID_COLUMNS:
                print("\nColumn is out of range, try again!")
                continue
            elif oth_const.GRID_FIELD_LIST[first_player_row_input-1][first_player_column_input-1] == oth_const.FIRST_PLAYER_SYMBOL:
                print("\nTry another position; your symbol is already in this one.")
                continue
            elif oth_const.GRID_FIELD_LIST[first_player_row_input-1][first_player_column_input-1] == oth_const.SECOND_PLAYER_SYMBOL:
                print("\nTry another position; your opponent's symbol is already in this one.")
                continue
            else:
                oth_const.GRID_FIELD_LIST[first_player_row_input-1][first_player_column_input-1] = oth_const.FIRST_PLAYER_SYMBOL
                print("\nGreat, " + str(oth_const.FIRST_PLAYER_NAME) + ", this position for your symbol '" + str(oth_const.FIRST_PLAYER_SYMBOL) + "' is still available.")
                print("I'm placing your symbol '" + str(oth_const.FIRST_PLAYER_SYMBOL) + "' in position --->\nrow: " + str(first_player_row_input) + "\ncolumn: " + str(first_player_column_input))
                break
        # decrease of symbol input/inserts options.
        number_of_options -= 1
        # display of the current playing field - grid
        print()
        grid_field.grid_field_during_duel()
        print()
        
        if number_of_options == 0:
            break
        
        sleep(1) 
        # second players input/insert symbol
        print("---- " + str(oth_const.SECOND_PLAYER_NAME) + " as a player number two chooses a position for their '" + str(oth_const.SECOND_PLAYER_SYMBOL) + "' symbol --->")    
        while True:
            second_player_row_input = input("Please select a ROW position number: ")
            second_player_column_input = input("Please select a COLUMN position number: ")

            try:
                second_player_row_input = int(second_player_row_input)
                second_player_column_input = int(second_player_column_input)
            except ValueError:
                print("\nPlease write only integers. Thanks.")
                continue
            if second_player_row_input < 1 or second_player_row_input > oth_const.GRID_ROWS:
                print("\nRow is out of range, try again!")
                continue
            elif second_player_column_input < 1 or second_player_column_input > oth_const.GRID_COLUMNS:
                print("\nColumn is out of range, try again!")
                continue
            elif oth_const.GRID_FIELD_LIST[second_player_row_input-1][second_player_column_input-1] == oth_const.SECOND_PLAYER_SYMBOL:
                print("\nTry another position; your symbol is already in this one.")
                continue
            elif oth_const.GRID_FIELD_LIST[second_player_row_input-1][second_player_column_input-1] == oth_const.FIRST_PLAYER_SYMBOL:
                print("\nTry another position; your opponent's symbol is already in this one.")
                continue
            else:
                oth_const.GRID_FIELD_LIST[second_player_row_input-1][second_player_column_input-1] = oth_const.SECOND_PLAYER_SYMBOL
                print("\nGreat, " + str(oth_const.SECOND_PLAYER_NAME) + ", this position for your symbol '" + str(oth_const.SECOND_PLAYER_SYMBOL) + "' is still available.")
                print("I'm placing your symbol '" + str(oth_const.SECOND_PLAYER_SYMBOL) + "' in position --->\nrow: " + str(second_player_row_input) + "\ncolumn: " + str(second_player_column_input))
                break
        # decrease of symbol input/inserts options.
        number_of_options -= 1
        # display of the current playing field - grid
        print()
        grid_field.grid_field_during_duel()
        print()
   