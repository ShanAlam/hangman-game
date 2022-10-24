import random
import hangman_art
import hangman_words

# Printing hangman ASCII art
print(hangman_art.logo)
print("\n")

# Getting all random words that can be chosen from
word_list = hangman_words.word_list

# Choosing a random word for the list of words
random_word = random.choice(word_list)

# Creating a list where the letters of the word will be held
placeholder = []

# Adding undersocres to display the number of letters in word to user
for i in range(len(random_word)):
  placeholder += "_"

# Variable used to determine if game is solved
solved = False

# Variable which holds number of lives remaining 
lives = len(hangman_art.stages) - 1 

# List which holds all the users guessed letters so that they dont renter them
guessed = []

while (solved == False) and (lives != 0):

  # Printing the placeholder 
  print(" ".join(placeholder), "\n")

  # Allowing user to pick a letter 
  choice = input("Pick a letter: ").lower()

  # Ensuring the user picks a letter which they have not already used
  while choice in guessed:
    choice = input(f"You already tried {choice}, pick another letter: ").lower()

  # Storing users chosen letter in the list of guessed letters 
  guessed.append(choice)

  wrong = 0

  # For each letter in the random word... 
  for i, letter in enumerate(random_word):

    # if the users choice is the same as the current letter...
    if choice == letter:
      # Replace the _ with the letter in the placeholder text
      placeholder[i] = letter
    # if the users choice is the not the same as the current letter...
    else:
      # add 1 to wrong 
      wrong += 1

  # If the number of wrong is the same as the length of the random word...
  # meaning that the letter was not in the word...
  if wrong == len(random_word):
    # Remove a life and print it on screen
    lives -= 1
    print(f"You guessed {choice}, that's not in the word, you have {lives} lives remaining")

  # If the placeholder text is the same as the random word it means the game is solved 
  if "".join(placeholder) == random_word:
    solved = True
    
  # Print the hangman art
  print(hangman_art.stages[lives])

  print("\n")

# Final game message depending on if the user found the word or not
if solved == True:
  print(" ".join(placeholder), "\n")
  print("Well done, you won!")
else:
  print(f"Sorry, you lost :(, the word you were looking for was {random_word}")