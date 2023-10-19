import phase_constatns as phase_const
from other_constants import SEPARATOR
from time import sleep


# assigning player names
def choose_names_for_players():
    sleep(1)
    print("\n\n\tNEW GAME\n" + SEPARATOR + "\nAt the beginning of the game, please enter the names and the playing symbols of the players.\n" + SEPARATOR)
    
    while True:
        first_player_name = input("Enter the name of the first player: ")
        if len(first_player_name) > 0:
            break
        else:
            print("\nEnter at least one character as the name for your player.")
            
    print("")
    
    while True:
        second_player_name = input("Enter the name of the second player: ")
        if len(second_player_name) > 0 and first_player_name != second_player_name:
            break
        elif first_player_name == second_player_name:
            print("\nPlease enter a different name than the player number one has.")
        elif len(second_player_name) <= 0:
            print("\nEnter at least one character as the name for your player.")
    
    print("\n\nAlright, so we have the name of the first player and the name of the second player.")
    print("First player's name:", first_player_name)
    print("Second player's second:", second_player_name)
    
    return choose_symbols_for_players(first_player_name, second_player_name)
    
    
# # assigning player symbols
def choose_symbols_for_players(first_player_n, second_player_n):
    sleep(1)
    print("\n\n" + SEPARATOR + "\nNext, please enter the playing symbols for the players.\n" + SEPARATOR)
    
    while True:
        first_player_symbol = input(str(first_player_n) + " write your unique one character playing symbol: ")
        if len(first_player_symbol) == 1:
            break
        else:
            print("\nEnter only one character as the name for your playing symbol.")

    print("")
    
    while True:
        second_player_symbol = input(str(second_player_n) + " write your unique one character playing symbol: ")
        if len(second_player_symbol) == 1 and first_player_symbol != second_player_symbol:
            break
        elif first_player_symbol == second_player_symbol:
            print("\nPlease enter a different name for symbol than the player number one has.")
        else:
            print("\nEnter only one character as the name for your playing symbol.")
    
    print("\n\nAlright, so we have the playing symbols of the players.")
    print(str(first_player_n) + "'s playing symbol:", first_player_symbol)
    print(str(second_player_n) + "'s playing symbol:", second_player_symbol)
    
    return what_next(first_player_n, second_player_n, first_player_symbol, second_player_symbol)
    

# battle or menu ?
def what_next(first_p_name, second_p_name, first_p_symbol, second_p_symbol):
    sleep(1)
    print("\n\n" + SEPARATOR)
    print("Okay, we have names and playing symbols for the players.")
    print(SEPARATOR)
    print("Do you want to continue to Play the Tic-Tac-Toe game,\nor do you want to go to Game Menu where you can choose to Save the Game or End the Game,\nor, from the menu you can choose 'Start a Completely New Game with New Players'.")
    print(SEPARATOR)
    
    choice_list_01 = ["Start the battle of wits", "Game Menu"]
    for number, choice in dict(enumerate(choice_list_01, 1)).items():
        print(number, "-", choice)
        
    while True:
        user_input = input("\nYour choice is: ")
        if user_input == "1":
            return first_p_name, second_p_name, first_p_symbol, second_p_symbol, phase_const.START_DUEL_PHASE
        elif user_input == "2":
            return first_p_name, second_p_name, first_p_symbol, second_p_symbol, phase_const.IN_GAME_MENU
        else:
            print("\nOut of range, try again!")
            continue
    