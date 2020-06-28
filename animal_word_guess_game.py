#Word Guessing Game
#Computer picks a random word
#Player tries to guess it
#computer only responds with yes or no

from random import choice


words = choice(('rabbit', 'cat', 'tiger', 'snake'))

#clue = words[0] + words[::-1][0]
clue = words[0] + words[-1]
word_guess = ''
store_letter = ''
count = 0
lives = 5

print('Welcome to "Guess the Word Animal Game!"')
print("Hi, you have 5 attempts at guessing the letters in the word")
print("Let's begin!")
print()

while count < lives:
    letter_guess = input('Guess a letter: ')
    count += 1

    if letter_guess in words:
        print('yes!')
        store_letter += letter_guess

    else:
        print('no!')

    if count == 2:
        print('\n')
        clue_request = input('Would you like a clue? [y / n] ')
        if clue_request == 'y':
            print('\n')
            print('CLUE: The first and last letter of the word is: ', clue)
        elif clue_request == 'n':
            print("You're brave!")

        print('\n')
        print('Now time to guess. You have guessed', len(store_letter), 'letters correctly.')
        print('These letters are: ', store_letter)

        word_guess = input('Guess the whole word: ')


        if word_guess.lower() == words:
            print('Congrats!')
        else:
            print('Unlucky! The answer was,', words)
        break # break statement exits the loop
