import other_constants as oth_const
from play_the_game.playing_the_game import playing_the_game
from time import sleep


def grid_field_for_new_game():
    
    print("This is the initial empty playing field --->\n")
    
    # create playing grid field list
    for row in range(oth_const.GRID_ROWS):
        oth_const.GRID_FIELD_LIST.append([])
        for column in range(oth_const.GRID_COLUMNS):
            oth_const.GRID_FIELD_LIST[row].append("_")
            
    # display of the empty playing grid field
    grid_field_during_duel()
    
    print()
    sleep(1)
    # start play the game
    playing_the_game()


# creating the playing field that will be displayed during the game
def grid_field_during_duel():
    print(end="  ")
    for column in range(oth_const.GRID_COLUMNS):
        print(column + 1, end=" ")
    print()
    for row in range(len(oth_const.GRID_FIELD_LIST)):
        print(row + 1, end=" ")
        for column in oth_const.GRID_FIELD_LIST[row]:
            print(column, end=" ")
        print()
