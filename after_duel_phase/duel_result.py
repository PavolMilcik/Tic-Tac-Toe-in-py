import phase_constatns as phase_const
import other_constants as oth_const
from other_constants import SEPARATOR
from after_duel_phase.count_players_wins import count_rows_win
from after_duel_phase.compare_number_of_wins import who_won_or_is_it_draw, print_some_statistics
from time import sleep

def duel_result():
    sleep(2)
    
    # count players wins in rows, columns and diagonals in acutal game
    count_rows_win()
    
    # name of the winner
    winner_is = who_won_or_is_it_draw()
    
    print("\n\n\tTHE GAME RESULT\n" + SEPARATOR)
    
    print("The winner of the duel between " + str(oth_const.FIRST_PLAYER_NAME) + " and " + str(oth_const.SECOND_PLAYER_NAME) +" is as follows --->")
    print(SEPARATOR)
    
    sleep(1)
    print("The triumphant champion of the super exciting brain game known as tic-tac-toe is:\n"  + str(winner_is.upper()))

    sleep(2)
    # printing some statistics about the actual game
    print_some_statistics(winner_is)
    
    sleep(3)
    print("\n\n" + SEPARATOR)
    print("Do you want to play another round between " + str(oth_const.FIRST_PLAYER_NAME) + " and " + str(oth_const.SECOND_PLAYER_NAME) + "?\nOr start a new game for two new players, save the statistics of this game, or end the game?")
    print(SEPARATOR)
    
    sleep(2)
    oth_const.FIRST_PLAYER_ACTUALL_GAME_WINS = 0
    oth_const.SECOND_PLAYER_ACTUALL_GAME_WINS = 0
    
    return phase_const.IN_GAME_MENU
 