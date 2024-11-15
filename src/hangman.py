from random import randint
"""
PROMPT: 

We are interested in building a small version of the word guessing game “Hangman”.

This is a game about guessing a secret word before running out of lives. 

The general flow of the game is that the user is shown a sequence of “empty letters” (represented by dashes) and prompted to guess a letter. When the user inputs a letter the game then either reveals the letter in the word or tells the user the letter is not present in the secret word and decrements a life.

The game is over when either the user guesses every letter in the secret word or loses all their lives.

Phase 2: Add support for phrases, where the secret word is actually many words and the spaces render as spaces not blanks

e.g. "abc def ghi" => "--- --- ---"

Phase 3: Construct the phrase from randomly picking 3 words from the dictionary

"""

dictionary = [
  'residence',
  'meal',
  'hilarious',
  'reflection',
  'check',
  'depressed',
  'chart',
  'discreet',
  'apology',
  'bin',
  'bang',
  'car',
  'migration',
  'doubt',
  'support',
  'tropical',
  'key',
  'pumpkin',
  'track',
  'opinion',
  'wind',
  'cute',
  'laborer',
]

def main():
  max_guesses = 3
  word = ' '.join([dictionary[randint(0, len(dictionary))] for i in range(0, 3)])
  # words_split = word.split(" ")
  masked_word = ["-" if c != " " else " " for c in word]
  print(f"masked_word: {masked_word}")
  while max_guesses > 0:
    user_input = input("enter the next char: ")
    contains = False
    # for w in words_split:
    if user_input in word:
      # find indices
      indices = [i for i in range(0, len(word)) if word[i] == user_input]
      # unmask
      for i in indices:
          masked_word[i] = user_input
      contains = True
      print(f"current: {''.join(masked_word)}")
    else:
      print(f"{user_input} not in word")
    if word == ''.join(masked_word):
      break
    if not contains:
      max_guesses -= 1
  if max_guesses <= 0:
    print("hangman")
  else:
    print("winner")


if __name__ == "__main__":
  main()
