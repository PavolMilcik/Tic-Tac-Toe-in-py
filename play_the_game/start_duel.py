from other_constants import SEPARATOR
import other_constants as oth_const
from play_the_game.grid_field import grid_field_for_new_game
from time import sleep


# entry information about players
def start_duel():
    print("\n\n\tDUEL\n" + SEPARATOR)
    
    print("The duel between " + str(oth_const.FIRST_PLAYER_NAME) + " and " + str(oth_const.SECOND_PLAYER_NAME) +" has just begun.\n" + str(oth_const.FIRST_PLAYER_NAME) + "'s playing symbol is '" + str(oth_const.FIRST_PLAYER_SYMBOL) + "' and " + str(oth_const.SECOND_PLAYER_NAME) + "'s is '" + str(oth_const.SECOND_PLAYER_SYMBOL) + "'.")
    
    if oth_const.FIRST_PLAYER_ALL_WINS > 0 or oth_const.SECOND_PLAYER_ALL_WINS > 0:
        print(str(oth_const.FIRST_PLAYER_NAME) + " has a total of this many victories:  " + str(oth_const.FIRST_PLAYER_ALL_WINS) + ".\n" + str(oth_const.SECOND_PLAYER_NAME) + " has a total of this many victories:  " + str(oth_const.SECOND_PLAYER_ALL_WINS) + ". ")
        
    print("Player number one is " + str(oth_const.FIRST_PLAYER_NAME) + ", and he goes first.")
    print(SEPARATOR + "\n")
    
    
    
    sleep(1)
    # creating a playing grid and playing the game
    grid_field_for_new_game()
