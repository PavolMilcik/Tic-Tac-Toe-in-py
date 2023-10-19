import other_constants as oth_const
import phase_constatns as phase_const
from other_constants import SEPARATOR
from save_load_game.loading_and_rewriting import loading_and_rewriting_game
from time import sleep
import os

def load_game():
    
    oth_const.FIRST_PLAYER_NAME = ""
    oth_const.SECOND_PLAYER_NAME = ""
    oth_const.FIRST_PLAYER_SYMBOL = ""
    oth_const.SECOND_PLAYER_SYMBOL = ""
    oth_const.FIRST_PLAYER_ALL_WINS = 0
    oth_const.SECOND_PLAYER_ALL_WINS = 0

    sleep(1)
    print("\n\n\tLOAD GAME\n" + SEPARATOR)
    
    list_of_files_in_directory = []
    dict_load_games = {}
    selected_load_game = ""
    
    # check if directory 'saved_games' is EXIST
    if os.path.isdir("save_load_game/saved_games/") is False:
        print("There are no Saved Games! Start the New Game!\n")
        return phase_const.MAIN_MENU_PHASE
    
    # check if directory 'saved_games' is EXIST
    elif os.path.isdir("save_load_game/saved_games/") is True:
        
        # check if directory 'saved_games' is EMPTY
        if not os.listdir("save_load_game/saved_games/"):
            print("There are no Saved Games! Start the New Game!\n")
            return phase_const.MAIN_MENU_PHASE
        
        # if directory 'saved_games' is NOT EMPTY
        elif os.listdir("save_load_game/saved_games/"):
            # create list of saved games from all saved files
            saved_games_files = os.listdir("save_load_game/saved_games/")
            for i in saved_games_files:
                find_py = i.find(".py")
                find_txt = i.find(".txt")
                if "py" in i:
                    list_of_files_in_directory.append(i[:find_py])
                elif "txt" in i:
                    list_of_files_in_directory.append(i[:find_txt])
                else:
                    list_of_files_in_directory.append(i)
                    
            # create dictionary of saved games from all saved files
            for j in range(len(list_of_files_in_directory)):
                dict_load_games[j] = list_of_files_in_directory[j]
    
    print("You can choose from these saved games --->")
    print(SEPARATOR)
    # choose saved game
    while True:        
        # print saved games to choose for the player
        print("0 - Go Back To Main Menu!\n")
        for k, v in dict_load_games.items():
            print(k+1, "-", v)
        
        user_load_game_input = input("\nWhich saved game do you want to load: ")
        
        if user_load_game_input == "0" or user_load_game_input == "Go Back!" or user_load_game_input == "Back":
            return phase_const.MAIN_MENU_PHASE

        if user_load_game_input.isdecimal() and user_load_game_input in dict_load_games.values():
            print("\nAn interesting situation has arisen.")
            print("Do you want to choose a game from the left side by order - 1\n,or from the right side by game name - 2 ?")
            if int(user_load_game_input) in dict_load_games.keys():
                while True:
                    user_input = input("\nYour choice is: ")
                    if user_input == "1":
                        user_load_game_input = int(user_load_game_input)
                        if user_load_game_input in dict_load_games.keys():
                            print("\nYou choose this game:", dict_load_games[user_load_game_input-1])
                            selected_load_game = dict_load_games[user_load_game_input-1]
                            break
                        else:
                            print("\nout of range, try again!!\n")
                            continue
                    elif user_input == "2":
                        selected_load_game = user_load_game_input
                        print("\nYou choose this game:", user_load_game_input)
                        break
                    else:
                        print("\nout of range, try again!\n")
                        continue
                break
            else:
                print("\nYou choose this game:", user_load_game_input)
                break
                               
        elif user_load_game_input.isdecimal() and user_load_game_input not in dict_load_games.values():
            user_load_game_input = int(user_load_game_input) - 1
            if user_load_game_input in dict_load_games.keys():
                print("\nYou choose this game:", dict_load_games[user_load_game_input])
                selected_load_game = dict_load_games[user_load_game_input]
                break
            else:
                print("\nout of range, try again!\n")
                continue
            
        elif user_load_game_input in dict_load_games.values():
                print("\nYou choose this game:", user_load_game_input)
                selected_load_game = user_load_game_input
                break
                
        else:
            print("\nout of range, try again!\n")
            continue
    
    loading_and_rewriting_game(selected_load_game)
    
    sleep(2)
    
    return phase_const.IN_GAME_MENU
       