from hangman import *
from wordle import *


def main():
    main_menu = True
    while main_menu == True:
        print("""
    What would you like to play :
    1. Hangman
    2. Wordle
    3. tic tac toe
            """)
        ans = input("Enter a value : ")

        match ans:
            case "1":
                hangman()
                main_back = input(
                    "Would you like to go back to the main menu (yes or no) : ").upper()
                if main_back == "YES":
                   continue
                else:
                    break
            case "2":
                wordle()
                main_back = input(
                    "Would you like to go back to the main menu (yes or no) : ").upper()
                if main_back == "YES":
                   continue
                else:
                    break


if __name__ == '__main__':
    main()
