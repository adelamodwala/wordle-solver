import json
from wordle import new_game, play, getRandomWord, getGameDict
import random

dict = getGameDict()

def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

def brute_stratagem(seed_word):
  if seed_word == None:
    seed_word = random.choice(list(dict))

  game_state = new_game()
  game_state = play(seed_word, game_state)
  if game_state == True:
    print("Answer found: " + seed_word)
  else:
    while game_state['tries'] > 0:
      matched_letters = game_state['letters']
      if len(list(matched_letters)) == 0:
        game_state = play(getRandomWord(), game_state)
      else:
        # find all words that contain all the letters in the matched_letters
        matched_letters_list = list(matched_letters)
        for candidate in dict:
          if len(intersection(candidate, matched_letters_list)) > 0:
            print(candidate)


game_state = new_game()
game_state['word'] = 'liver'
print(game_state)
game_state = play("sleek", game_state)
print(game_state)
game_state = play("train", game_state)
print(game_state)