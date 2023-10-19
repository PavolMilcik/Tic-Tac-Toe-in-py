import other_constants as oth_const

   
def count_rows_win():
    for i in oth_const.GRID_FIELD_LIST:
        count_first_p_symbol = 0
        count_second_p_symbol = 0
        for j in i:
            if j == oth_const.FIRST_PLAYER_SYMBOL:
                count_first_p_symbol += 1
            elif j == oth_const.SECOND_PLAYER_SYMBOL:
                count_second_p_symbol += 1
        if count_first_p_symbol == oth_const.GRID_ROWS:
            oth_const.FIRST_PLAYER_ALL_WINS += 1
            oth_const.FIRST_PLAYER_ACTUALL_GAME_WINS += 1
        elif count_second_p_symbol == oth_const.GRID_ROWS:
            oth_const.SECOND_PLAYER_ALL_WINS += 1
            oth_const.SECOND_PLAYER_ACTUALL_GAME_WINS += 1
    
    count_columns_win()


def count_columns_win():
    for column in range(oth_const.GRID_COLUMNS):
        count_first_p_symbol = 0
        count_second_p_symbol = 0
        for row in range(oth_const.GRID_ROWS):
            if oth_const.GRID_FIELD_LIST[row][column] == oth_const.FIRST_PLAYER_SYMBOL:
                count_first_p_symbol += 1
            elif oth_const.GRID_FIELD_LIST[row][column] == oth_const.SECOND_PLAYER_SYMBOL:
                count_second_p_symbol += 1
        if count_first_p_symbol == oth_const.GRID_COLUMNS:
            oth_const.FIRST_PLAYER_ALL_WINS += 1
            oth_const.FIRST_PLAYER_ACTUALL_GAME_WINS += 1
        elif count_second_p_symbol == oth_const.GRID_COLUMNS:
            oth_const.SECOND_PLAYER_ALL_WINS += 1
            oth_const.SECOND_PLAYER_ACTUALL_GAME_WINS += 1
            
    count_diagolans_front_to_back_win()


def count_diagolans_front_to_back_win():
    count_diagonal_front_to_back_first_p_symbol = 0
    count_diagonal_front_to_back_second_p_symbol = 0
    for row in range(oth_const.GRID_ROWS):
        for column in range(row, oth_const.GRID_COLUMNS):
            if oth_const.GRID_FIELD_LIST[row][column] == oth_const.FIRST_PLAYER_SYMBOL:
                count_diagonal_front_to_back_first_p_symbol += 1
            elif oth_const.GRID_FIELD_LIST[row][column] == oth_const.SECOND_PLAYER_SYMBOL:
                count_diagonal_front_to_back_second_p_symbol += 1
            break
    if count_diagonal_front_to_back_first_p_symbol == oth_const.GRID_COLUMNS:
        oth_const.FIRST_PLAYER_ALL_WINS += 1
        oth_const.FIRST_PLAYER_ACTUALL_GAME_WINS += 1
    elif count_diagonal_front_to_back_second_p_symbol == oth_const.GRID_COLUMNS:
        oth_const.SECOND_PLAYER_ALL_WINS += 1
        oth_const.SECOND_PLAYER_ACTUALL_GAME_WINS += 1
    
    count_diagolans_back_to_front_win()


def count_diagolans_back_to_front_win():
    count_diagonal_back_to_front_first_p_symbol = 0
    count_diagonal_back_to_front_second_p_symbol = 0
    for row in range(oth_const.GRID_ROWS):
        for column in range(oth_const.GRID_COLUMNS-1-row, -1, -1):
            if oth_const.GRID_FIELD_LIST[row][column] == oth_const.FIRST_PLAYER_SYMBOL:
                count_diagonal_back_to_front_first_p_symbol += 1
            elif oth_const.GRID_FIELD_LIST[row][column] == oth_const.SECOND_PLAYER_SYMBOL:
                count_diagonal_back_to_front_second_p_symbol += 1
            break
    if count_diagonal_back_to_front_first_p_symbol == oth_const.GRID_COLUMNS:
        oth_const.FIRST_PLAYER_ALL_WINS += 1
        oth_const.FIRST_PLAYER_ACTUALL_GAME_WINS += 1
    elif count_diagonal_back_to_front_second_p_symbol == oth_const.GRID_COLUMNS:
        oth_const.SECOND_PLAYER_ALL_WINS += 1
        oth_const.SECOND_PLAYER_ACTUALL_GAME_WINS += 1
