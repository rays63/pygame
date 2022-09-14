import random
import string
from words import Words
from visual import lives as hang

def get_words(Word):
    word = random.choice(Word)
    return word.upper()

def hangman():
    play = True
    while play == True:
        word = get_words(Words)
        word_letter = set(word)
        alphabet = set(string.ascii_uppercase)
        used_letters = set()
        lives = 7

        print("Welcome to HangMan")

        while len(word_letter) > 0  and lives >0:
            print('You have ', lives, 'lives left. ','You have used these letters : ', ' '.join(used_letters))
            print(hang[lives])

            word_list = [letter if letter in used_letters else '-' for letter in word]
            print("Current Word : ", " ".join(word_list))

            user_input = input('Guess a letter : ').upper()

            while len(user_input) != 1:
                print('Enter a valid letter !')
                user_input = input('Guess a letter : ').upper()
            
            if user_input in alphabet - used_letters:
                used_letters.add(user_input)
                if user_input in word_letter:
                    word_letter.remove(user_input)
                else:
                    lives = lives - 1
                    print("Letter is not in Word.")


            elif user_input in used_letters:
                print("You have already used this letter already!")
        
        if lives == 0:
            print('Sorry, You died the word was ', word)
            print(hang[lives])
        else:
            print('Congratulations!! You guessed the word ', word)
        
        play = False
        play_again = input("Do you want to play again ?  Yes or No  -> ").upper()

        if play_again == "YES":
            play = True
        else:
            play = False

            