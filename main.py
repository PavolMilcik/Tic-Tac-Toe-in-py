# This is the main file of the whole project - the game - Tic-Tac-Toe.
import phase_constatns as phase_const
import other_constants as oth_const
from phases_of_the_game.intro import intro_print
from phases_of_the_game.main_menu import menu_selection
from phases_of_the_game.names_symbols_for_new_game import choose_names_for_players
from phases_of_the_game.in_game_menu import in_game_menu
from play_the_game.initial_settings_of_grid import initial_settings_of_grid
from after_duel_phase.duel_result import duel_result
from phases_of_the_game.end_the_game import end_the_game
from save_load_game.save_game import save_game
from save_load_game.load_game import load_game



# intro of the program, phase --->
current_phase = phase_const.INTRO_PHASE

while True:
    # intro phase --->
    if current_phase == phase_const.INTRO_PHASE:
        current_phase = intro_print()
    
    # main menu, before the game, phase --->
    elif current_phase == phase_const.MAIN_MENU_PHASE:
        current_phase = menu_selection()
    
    # start the new game by entering a name and a symbol., phase --->
    elif current_phase == phase_const.NAMES_SYMBOLS_FOR_NEW_GAME_PHASE:
        oth_const.FIRST_PLAYER_NAME, oth_const.SECOND_PLAYER_NAME, oth_const.FIRST_PLAYER_SYMBOL, oth_const.SECOND_PLAYER_SYMBOL, current_phase = choose_names_for_players()
        
    # in the game - menu phase --->
    elif current_phase == phase_const.IN_GAME_MENU:
        current_phase = in_game_menu()
    
    # if name and symbol are entered, start duel phase --->
    elif current_phase == phase_const.START_DUEL_PHASE:
        current_phase = initial_settings_of_grid()
        
    # check who won the duel, or if it's a draw, after duel phase --->
    elif current_phase == phase_const.AFTER_DUEL_PHASE:
        current_phase = duel_result()
    
    # save game phase --->    
    elif current_phase == phase_const.SAVE_GAME_PHASE:
        current_phase = save_game()
    
    # load game phase --->
    elif current_phase == phase_const.LOAD_GAME_PHASE:
        current_phase = load_game()
        
    # end the game phase --->    
    elif current_phase == phase_const.END_GAME_PHASE:
        end_the_game()
        break
