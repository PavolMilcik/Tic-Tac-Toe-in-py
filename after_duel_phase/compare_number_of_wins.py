import other_constants as oth_const
from play_the_game.grid_field import grid_field_during_duel


# compare the number of wins in actual game and determine the winner:
def who_won_or_is_it_draw():
    if oth_const.FIRST_PLAYER_ACTUALL_GAME_WINS > oth_const.SECOND_PLAYER_ACTUALL_GAME_WINS:
        return oth_const.FIRST_PLAYER_NAME
    elif oth_const.FIRST_PLAYER_ACTUALL_GAME_WINS < oth_const.SECOND_PLAYER_ACTUALL_GAME_WINS:
        return oth_const.SECOND_PLAYER_NAME
    elif oth_const.FIRST_PLAYER_ACTUALL_GAME_WINS == oth_const.SECOND_PLAYER_ACTUALL_GAME_WINS:
        return "There was a draw in the game between " + str(oth_const.FIRST_PLAYER_NAME) + " and " + str(oth_const.SECOND_PLAYER_NAME) + "."
    
    
# printing some statistics about the actual game    
def print_some_statistics(winner_is):
    
    if winner_is == oth_const.FIRST_PLAYER_NAME:
        if oth_const.FIRST_PLAYER_ACTUALL_GAME_WINS > 1:
            print("\n" + str(winner_is) + " has " + str(oth_const.FIRST_PLAYER_ACTUALL_GAME_WINS) + " wins, in this game.")
        else:
            print("\n" + str(winner_is) + " has " + str(oth_const.FIRST_PLAYER_ACTUALL_GAME_WINS) + " win, in this game.")
        if oth_const.SECOND_PLAYER_ACTUALL_GAME_WINS > 0:
            print(str(oth_const.SECOND_PLAYER_NAME) + " has " + str(oth_const.SECOND_PLAYER_ACTUALL_GAME_WINS) + " win, in this game.")
            
    elif winner_is == oth_const.SECOND_PLAYER_NAME:
        if oth_const.SECOND_PLAYER_ACTUALL_GAME_WINS > 1:
            print("\n" + str(winner_is) + " has " + str(oth_const.SECOND_PLAYER_ACTUALL_GAME_WINS) + " wins, in this game.")
        else:
            print("\n" + str(winner_is) + " has " + str(oth_const.SECOND_PLAYER_ACTUALL_GAME_WINS) + " win, in this game.")
        if oth_const.FIRST_PLAYER_ACTUALL_GAME_WINS > 0:
            print(str(oth_const.FIRST_PLAYER_NAME) + " has " + str(oth_const.FIRST_PLAYER_ACTUALL_GAME_WINS) + " win, in this game.")
            
    else:
        print("\n" + str(oth_const.FIRST_PLAYER_NAME) + " has " + str(oth_const.FIRST_PLAYER_ACTUALL_GAME_WINS) + " win, in this game.")
        print(str(oth_const.SECOND_PLAYER_NAME) + " has " + str(oth_const.SECOND_PLAYER_ACTUALL_GAME_WINS) + " win, in this game.")
             
    print("\n... and this is what the final playing grid looks like --->\n")
    grid_field_during_duel()
    print("\n" + str(oth_const.FIRST_PLAYER_NAME) + "'s playing symbol is '" + str(oth_const.FIRST_PLAYER_SYMBOL) + "' and " + str(oth_const.SECOND_PLAYER_NAME) + "'s is '" + str(oth_const.SECOND_PLAYER_SYMBOL) + "'")

    
    if oth_const.FIRST_PLAYER_ALL_WINS > 0:
        print("\n" + str(oth_const.FIRST_PLAYER_NAME) + " has a total of this number of wins: " + str(oth_const.FIRST_PLAYER_ALL_WINS))
    if oth_const.SECOND_PLAYER_ALL_WINS > 0:
        print(str(oth_const.SECOND_PLAYER_NAME) + " has a total of this number of wins: " + str(oth_const.SECOND_PLAYER_ALL_WINS))
