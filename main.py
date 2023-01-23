# module that have randomization feature
import random

# module that helps interact with operation systems
import os

import getWord.getWord1 as getWord              # module that get words

# running get.py program that write visualLives.py program
from getVisualLives import get

# importing visualLives.py that contain live visualization
from getVisualLives import visualLives


words = getWord.word                            # get words
word = random.choice(words)                     # choose a word randomly
guessed_word = ''
guessed_letter = ''

lives = 6
pic = visualLives.lives_visual_dict             # live visualization dict


def processingQuestion():
    """This function will process the question
    based on letter that guessed by user
    """

    global guessed_word, guessed_letter         # enable to use global variable
    guessed_word = ''

    for letter in word:
        if letter in guessed_letter:                # if the letter have guessed
            guessed_word = guessed_word + letter
        else:                                       # if the letter not yet guessed
            guessed_word = guessed_word + '_'


processingQuestion()

while lives != 0:
    os.system('cls')

    print('HANGMAN GAME'.center(50), '\n')
    print(f'You only have {lives} chance to guess\n')

    # displaying live visualization
    print(pic[lives])
    # displaying the question
    print(*(i for i in guessed_word), sep=' ')

    if guessed_word == word:                            # check if the word already guessed
        break

    try:
        inp_letter = input('Guess a Letter > ').lower()

        if inp_letter.isnumeric():                          # user input number
            raise ValueError
        if len(inp_letter) != 1:                            # user input more than one letter
            raise Exception

    except ValueError:
        print('\nJust input a letter not number !\n')
        os.system('pause')
        continue
    except Exception:
        print('\nJust input a letter !\n')
        os.system('pause')
        continue

    # the letter is in the word and not yet guessed
    if inp_letter in word and inp_letter not in guessed_letter:
        guessed_letter += inp_letter
        print('One letter guessed\n\n')

    else:
        lives -= 1
        print(f'There is no letter {inp_letter} in the word')
        print(f'You have {lives} chance left\n\n')

    processingQuestion()

if lives != 0:
    print("You Won, Congratulations")
else:
    print('You Lose')
    print('The word > ', end=' ')
    print(*(i for i in word), sep=' ')
