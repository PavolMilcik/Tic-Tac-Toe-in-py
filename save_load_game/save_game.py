import phase_constatns as phase_const
import other_constants as oth_const
from other_constants import SEPARATOR
from time import sleep


def save_game():
    print("\n\n\tSAVE GAME\n" + SEPARATOR)
    
    sleep(1)
    
    print("How do you want to name the saved game?\n" + SEPARATOR)
    while True:
        user_input_save_game = input("Name of the saved game: ")
        if len(user_input_save_game) > 0 and user_input_save_game != "0":
            user_input_save_game.encode(encoding="utf-8")
            break
        else:
            print("The name of the saved game must contain at least one character, but it cannot be char 0!")
            continue
    
    sleep(1)
        
    file_handler_save_game = open("save_load_game/saved_games/" + str(user_input_save_game) + ".txt", "w", encoding="utf-8")
    
    # First Player Saved Info:
    file_handler_save_game.write("First Player Saved Info:\n")
    # save First player Name
    file_handler_save_game.write("name - " + str(oth_const.FIRST_PLAYER_NAME) + "\n")
    # save First player Symbol
    file_handler_save_game.write("symbol - " + str(oth_const.FIRST_PLAYER_SYMBOL) + "\n")
    # save First player Wins
    file_handler_save_game.write("number of wins - " + str(oth_const.FIRST_PLAYER_ALL_WINS) + "\n\n")
    
    # Second Player Saved Info:
    file_handler_save_game.write("Second Player Saved Info:\n")
    # save Second player Name
    file_handler_save_game.write("name - " + str(oth_const.SECOND_PLAYER_NAME) + "\n")
    # save Second player Symbol
    file_handler_save_game.write("symbol - " + str(oth_const.SECOND_PLAYER_SYMBOL) + "\n")
    # save Second player Wins
    file_handler_save_game.write("number of wins - " + str(oth_const.SECOND_PLAYER_ALL_WINS))
    
    file_handler_save_game.close()
    
    print("------ Your game is saved with this name: " + str(user_input_save_game))
    
    return phase_const.IN_GAME_MENU
