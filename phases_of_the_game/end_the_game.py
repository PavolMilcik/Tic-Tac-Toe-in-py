from other_constants import SEPARATOR
import other_constants as oth_const
from time import sleep


def end_the_game():
    sleep(1)
    print("\n\n\tEND THE GAME\n" + SEPARATOR)
    if oth_const.FIRST_PLAYER_NAME and oth_const.SECOND_PLAYER_ALL_WINS:
        print("Thank you for the game and battle of wits, " + str(oth_const.FIRST_PLAYER_NAME) + " and " + str(oth_const.SECOND_PLAYER_NAME) + ".")
        print("Hopefully, we'll see each other again sometime.\nHave a great day.\n\n")
    else:
        print("Hopefully, we'll see each other again sometime.\nHave a great day.\n\n")
    