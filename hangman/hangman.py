import random
from words import words
import string


def get_word(words):
    word = random.choice(words)  
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_word(words)
    letters = set(word)  
    alphabet = set(string.ascii_uppercase)
    used_letters = set() 
    lives = 6

    
    while len(letters) > 0 and lives > 0:
        
        print('You have', lives, 'lives left & you have used the letters: ', ' '.join(used_letters))

        
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in letters:
                letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1  # takes away a life if wrong
                print('\nthe letter,', user_letter, 'is not in the word.')

        elif user_letter in used_letters:
            print('\nYou have already used that letter. Guess another letter.')

        else:
            print('\n not a valid letter.')

    # gets here when len(letters) == 0 OR when lives == 0
    if lives == 0:
        print('You lost. The word was', word)
    else:
        print('You won!! the word was :', word, '!!')


if __name__ == '__main__':
    hangman()