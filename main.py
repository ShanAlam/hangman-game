import random
import hangman_art
import hangman_words

print(hangman_art.logo)
print("\n")

word_list = hangman_words.word_list

random_word = random.choice(word_list)

placeholder = []

for i in range(len(random_word)):
  placeholder += "_"

solved = False

lives = len(hangman_art.stages) - 1 

guessed = []

while (solved == False) and (lives != 0):

  print(" ".join(placeholder), "\n")

  choice = input("Pick a letter: ").lower()
  
  while choice in guessed:
    choice = input(f"You already tried {choice}, pick another letter: ").lower()
    
  guessed.append(choice)
  
  wrong = 0
  
  for i, letter in enumerate(random_word):
    if choice == letter:
      placeholder[i] = letter
    else:
      wrong += 1

  if wrong == len(random_word):
    lives -= 1
    print(f"You guessed {choice}, that's not in the word, you have {lives} lives remaining")

  if "".join(placeholder) == random_word:
    solved = True
    
  print(hangman_art.stages[lives])

  print("\n")

if solved == True:
  print(" ".join(placeholder), "\n")
  print("Well done, you won!")
else:
  print(f"Sorry, you lost :(, the word you were looking for was {random_word}")