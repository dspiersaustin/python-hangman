#Hangman game - start with hitting F5

import random

#Global variables
words = ['dog', 'cat', 'mouse', 'elephant','frog', 'bat']
lives_remaining = 14
guessed_letters  = ' '

#debug
debug = 'no'

# define our clear function
def clear():
    print ("\n" * 38)

#Functions
def play():
    #ask player 1 to enter words for player 2
    response = input('To enter word for other player enter a (1) to use built in words enter a (2): ')
    if response == '1':
        word = input('Enter word for other player ')
        #clear the screen
        clear()
        print ('Word has been set.  Time for player 2 to start:')

    elif response == '2':
        print ('Picking a word at random for you...')
        word = pick_a_word()
    else:
        print ('You did not select (1) or (2) so I will pick a word for you...')
        word = pick_a_word()

    #debug
    if debug == 'yes':
        print('debug mode word= ', word)
    
    while True:
        guess = get_guess(word)

        #debug
        if debug == 'yes':
            print('debug mode guess= ', guess)
        
        if process_guess(guess, word):
            print('You Win! Well done!  The word was ' + word)
            break
        if lives_remaining == 0:
            print('Game over.  You lose!')
            print('The word was: ' + word)
            break
        
def pick_a_word():
    return random.choice(words)

def get_guess(word):
    #global lives_remaining
    print_word_with_blanks(word)
    print ('Lives Remaining: ' + str(lives_remaining))
    guess = input('Guess a letter or whole word? ')
    return guess

#print current state of guesses i.e. [_ a _] after 1 guess of "a" for cat
def print_word_with_blanks(word):
    #global guessed_letters
    display_word = ''
    for letter in word:
        if guessed_letters.find(letter) > -1:
            #letter found
            display_word = display_word + letter
        else:
            #letter not found
            display_word = display_word + '-'
    print (display_word)

def process_guess(guess, word):
    if len(guess) > 1:
        return whole_word_guess(guess,word)
    else:
        return single_letter_guess(guess,word)

def whole_word_guess(guess,word):
    global lives_remaining
    if guess == word:
        return True
    else:
        lives_remaining = lives_remaining - 1
        return False    

def single_letter_guess(guess,word):
    global guessed_letters
    global lives_remaining
    if word.find(guess) == -1:
        #letter guess was incorrect
        lives_remaining = lives_remaining - 1
    guessed_letters = guessed_letters + guess
    if all_letters_guessed(word):
        return True
    return False

def all_letters_guessed(word):
    for letter in word:
        if guessed_letters.find(letter) == -1:
            return False
    return True


#Program Start
print ('-----------------------------------------------------')
print ('The game is Hangman')
print ('-----------------------------------------------------')
print (' ')

play()
#Program End

        
        
