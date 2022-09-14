from hangman import *
from wordle import *


def main():
    main_menu = True
    while main_menu == True:
        print("""
    What would you like to play :
    1. Hangman
    2. Wordle
    3. Tic tac toe
    X. exit
            """)
        ans = input("Enter a value : ").upper()

        match ans:
            case "1":
                hangman()
                main_back = input(
                    "Would you like to go back to the main menu (yes or no) : ").upper()
                if main_back == "YES":
                    print("\033c")
                    continue
                else:
                    break
            case "2":
                wordle()
                main_back = input(
                    "Would you like to go back to the main menu (yes or no) : ").upper()
                if main_back == "YES":
                    print("\033c")
                    continue
                else:
                    main_menu = False
            case "3":
                print('This game is still under development!!! please chose another game !')
                continue
            case "X":
                break
    print("Thank you for playing! \n")
            
if __name__ == '__main__':
    main()
