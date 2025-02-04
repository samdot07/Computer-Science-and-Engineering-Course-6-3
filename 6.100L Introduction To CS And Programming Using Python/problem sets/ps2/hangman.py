import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------

# Uncomment and change the path to where words.txt is
# WORDLIST_FILENAME = '/Users/username/6.100L Introduction To CS And Programming Using Python/ps2/words.txt'

def load_words():
    '''
    #### Returns:
    list, a list of valid words. Words are strings of lowercase letters.
    
    ---
    #### Note:
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(" ", len(wordlist), "words loaded.")
    
    return wordlist

def choose_word(wordlist):
  '''
  - wordlist (list): list of words (strings)
  ---
  #### Returns: 
    word from wordlist at random
  '''
  return random.choice(wordlist)

# -----------------------------------
# END OF HELPER CODE
# -----------------------------------


# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()

# -----------------------------------
# GAME SETUP
# -----------------------------------

def has_player_won(secret_word, letters_guessed):
  '''
  - secret_word: string, the lowercase word the user is guessing.
  - letters_guessed: list (of lowercase letters), the letters that have been
    guessed so far.
  ---
  #### Returns: 
    boolean, True if all the letters of secret_word are in letters_guessed,
    False otherwise.
  '''
  # Check if 
  # any letters in secret_word is not guessed, return False.
  # all letters in secret_word are guessed, return True.
  
  # Iterate through each character in secret_word
  for c in secret_word:
    if c not in letters_guessed:
      return False
  
  return True

def get_word_progress(secret_word, letters_guessed):
  '''
  - secret_word: string, the lowercase word the user is guessing.
  - letters_guessed: list (of lowercase letters), 
    the letters that have been guessed so far.
  ---
  #### Returns: 
    string, comprised of letters and asterisks (*) that represents
    which letters in secret_word have not been guessed so far.
  '''
  # If the current letter has been guessed add it to the empty string.
  # Otherwise, add '*' to represent the ungessed letter.
  # Return the final string.
  guess = ''
  
  # Iterate through each character in secret_word
  for c in secret_word:
    if c in letters_guessed:
      guess += c
    
    else:
      guess += '*'
  
  return guess
    
def get_available_letters(letters_guessed):
  '''
  - letters_guessed: list (of lowercase letters), the letters that have been
    guessed so far.
  ---
  #### Returns: 
    string, comprised of letters that represents which
    letters have not yet been guessed. The letters should be returned in
    alphabetical order.
  '''
  # Iterate through each letter in the alphabet [string.ascii_lowercase] and check if
  # the letter has not been guessed, add it to the list.
  # Return the string of available letters not guessed yet.
  available_letters = []

  # Iterate through all lowercase letters in the alphabet
  for c in string.ascii_lowercase:
    if c not in letters_guessed:
      available_letters.append(c)
  
  return ''.join(available_letters)

def with_help_func(secret_word, available_letters):
  '''
  - secret_word: string, the lowercase word the user is guessing.
  - available_letters: string, comprised of letters that represents which
    letters have not yet been guessed.
  ---
  #### Returns: 
    string, revealed_letter which represents the 
    letter that has been revealed.
  '''
  # Chek if
  # the letter is not in available_letters, it means it hasn't been guessed yet, append it to the list.
  # there are any letters in the choose_from list, randomly pick one to reveal.
  # Return the revealed letter.
  choose_from = []
  
  # Iterate through each character in secret_word
  for c in secret_word:
    if c not in available_letters:
      choose_from.append(c)
    
  if choose_from:
      new = random.randint(0, len(choose_from) - 1)
      revealed_letter = choose_from[new]
      
      return revealed_letter

# -----------------------------------
# THE GAME
# -----------------------------------

def hangman(secret_word, with_help=True):
  '''
  - secret_word: string, the secret word to guess.
  - with_help: boolean, this enables help functionality if true.
  ---
  ### Starts up an interactive game of Hangman
  - At the start of the game, let the user know how many
    letters the secret_word contains and how many guesses they start with.

  - The user should start with 10 guesses.

  - Before each round, you should display to the user how many guesses
    they have left and the letters that the user has not yet guessed.

  - Ask the user to supply one guess per round. Remember to make
    sure that the user puts in a single letter (or help character '!'
    for with_help functionality)

  - If the user inputs an incorrect consonant, then the user loses ONE guess,
    while if the user inputs an incorrect vowel (a, e, i, o, u),
    then the user loses TWO guesses.

  - The user should receive feedback immediately after each guess
    about whether their guess appears in the computer's word.

  - After each guess, you should display to the user the
    partially guessed word so far.

  ---
  ### with_help functionality
  - If the guess is the symbol !, you should reveal to the user one of the
    letters missing from the word at the cost of 3 guesses. If the user does
    not have 3 guesses remaining, print a warning message. Otherwise, add
    this letter to their guessed word and continue playing normally.

  Follows the other limitations detailed in the problem write-up.
  '''
  # Setup:
  # The user starts with 10 guesses.
  # Display the length of the secret word.
  # Display the remaining guesses and avalable letters.
  
  # Calculate the score by considering the number of guesses left,
  # the number of unique letters in the secret word,
  # and the total length of the secret word.
  
  # Check if
  # the help option is enabled, reveal a letter at the cost of 3 guesses, update letters_guessed.
  # not enough guesses for help, print a warning message.
  # the user has already guessed this letter.
  # the guess is a single letter from the alphabet.
  # Update the guessed letters with the current guess. If
  # the guessed letter is in the secret word, display progress.
  # the guess is incorrect, reduce guesses and give feedback.
  letters_guessed = []
  vowels = 'aeiou'
  guess_num = 10
  
  total_score = lambda secret_word, guess_num: (guess_num + 4 * len(set(secret_word)) + (3*len(secret_word)))

  print('Welcome to Hangman!\n'
        f'I am thinking of a word that is {len(secret_word)} letters long.'
      )
  
  # Loop until the player has guesses left
  while guess_num > 0:
    if has_player_won(secret_word, letters_guessed):
      print('----------------\n'
            f'Congratulations, you won! {secret_word}\n'
            f'Your total score for this game is: {total_score(secret_word, guess_num)}'
          )
      
      return

    print('----------------\n'
          f'You have {guess_num} guesses left.\n'
          f'Available letters: {get_available_letters(letters_guessed)}'
        )

    guess = input('Please guess a letter: ').lower()
    if with_help == True and guess == '!' and guess_num >= 3:
      guess_num -= 3
      revealed_letter = with_help_func(secret_word, letters_guessed)
      if revealed_letter:
        letters_guessed.append(revealed_letter)
        print(f'Letter revealed: {revealed_letter}\n'
              f'{get_word_progress(secret_word, letters_guessed)}'
            )
    
    elif guess == '!' and guess_num < 3:
      print(f'Oops! Not enough guesses left: {get_word_progress(secret_word, letters_guessed)}')

    if guess in letters_guessed:
      print(f'Oops! You have already guessed that letter: {get_word_progress(secret_word, letters_guessed)}')
    
    elif len(guess) != 1 or guess not in string.ascii_lowercase:
      if guess != '!':
        print(f'Oops! That is not a valid letter. '
              f'Please input a letter from the alphabet: {get_word_progress(secret_word, letters_guessed)}'
            )
      
      elif with_help == False and guess == '!':
        print(f'Oops! That is not a valid letter. '
              f'Please input a letter from the alphabet: {get_word_progress(secret_word, letters_guessed)}'
            )

    else:
      letters_guessed.append(guess)
      if guess in secret_word:
        print(f'Good guess: {get_word_progress(secret_word, letters_guessed)}')
      
      else:
        if guess in vowels:
          guess_num -= 2
        
        else:
          guess_num -= 1
        print(f'Oops! That letter is not in my word: {get_word_progress(secret_word, letters_guessed)}')

  if guess_num == 0:
    print('----------------\n'
          f'Sorry, you ran out of guesses. The word was {secret_word}.'
        )
    
    return

if __name__ == "__main__":
    # To test the game.
    secret_word = choose_word(wordlist)
    with_help = False
    hangman(secret_word, with_help)

    # After you complete with_help functionality, change with_help to True
    # and try entering "!" as a guess!