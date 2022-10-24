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
wrong_counter = 0

while (solved == False) and (wrong_counter != 7):

  print(" ".join(placeholder), "\n")
  choice = input("Pick a letter: ").lower()
  
  wrong = 0
  
  for i, letter in enumerate(random_word):
    if choice == letter:
      placeholder[i] = letter
    else:
      wrong += 1
  
  if wrong == len(random_word):
    wrong_counter += 1
    print(hangman_art.stages[-wrong_counter])

  if "".join(placeholder) == random_word:
    solved = True

  print("\n\n\n")

if solved == True:
  print(" ".join(placeholder), "\n")
  print("Well done, you won!")
else:
  print("Sorry, you lost :(")