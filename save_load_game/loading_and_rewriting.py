import other_constants as oth_const
from other_constants import SEPARATOR
from time import sleep


def loading_and_rewriting_game(selected_game):
    
    sleep(1)
    print("\n\n\tLOADING GAME AND REWRITING GAME INFO\n" + SEPARATOR)
    print("loaded game: " + str(selected_game) + "\n")
    
    file_handler_loading_game = open("save_load_game/saved_games/" + str(selected_game) + ".txt", "r", encoding="utf-8")
     
    for line in file_handler_loading_game:
        line = line.strip()
        # load and rewrite Players Names
        if "name" in line:
            if len(oth_const.FIRST_PLAYER_NAME) == 0:
                find_dash = line.find("-")
                name_first_player = line[find_dash+2:]
                oth_const.FIRST_PLAYER_NAME = name_first_player
            elif not oth_const.SECOND_PLAYER_NAME:
                find_dash = line.find("-")
                name_second_player = line[find_dash+2:]
                oth_const.SECOND_PLAYER_NAME = name_second_player
        # load and rewrite Players Symbols
        elif "symbol" in line:
            if len(oth_const.FIRST_PLAYER_SYMBOL) == 0:
                find_dash = line.find("-")
                symbol_first_player = line[find_dash+2:]
                oth_const.FIRST_PLAYER_SYMBOL = symbol_first_player
            elif not oth_const.SECOND_PLAYER_SYMBOL:
                find_dash = line.find("-")
                symbol_second_player = line[find_dash+2:]
                oth_const.SECOND_PLAYER_SYMBOL = symbol_second_player
        # load and rewrite Players All Wins
        elif "number of wins" in line:
            if oth_const.FIRST_PLAYER_ALL_WINS == 0:
                find_dash = line.find("-")
                wins_first_player = line[find_dash+2:]
                oth_const.FIRST_PLAYER_ALL_WINS = int(wins_first_player)
            elif not oth_const.SECOND_PLAYER_ALL_WINS:
                find_dash = line.find("-")
                wins_second_player = line[find_dash+2:]
                oth_const.SECOND_PLAYER_ALL_WINS = int(wins_second_player)
    
    file_handler_loading_game.close()
    sleep(1)
    
    print("First Player Loaded Info --->")
    print("name - " + str(oth_const.FIRST_PLAYER_NAME))
    print("symbol - " + str(oth_const.FIRST_PLAYER_SYMBOL))
    print("number of all wins - " + str(oth_const.FIRST_PLAYER_ALL_WINS) + "\n")
    
    print("Second Player Loaded Info --->")
    print("name - " + str(oth_const.SECOND_PLAYER_NAME))
    print("symbol - " + str(oth_const.SECOND_PLAYER_SYMBOL))
    print("number of all wins - " + str(oth_const.SECOND_PLAYER_ALL_WINS))
    
    sleep(1)
    print("\nThe game has loaded. Welcome back in game, " + str(oth_const.FIRST_PLAYER_NAME) + " and " + str(oth_const.SECOND_PLAYER_NAME) + ".\n")
