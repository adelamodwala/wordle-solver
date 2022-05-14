import json
import random

'''
Iterate over all the key value pairs in dictionary and call the given
callback function() on each pair. Items for which callback() returns True,
add them to the new dictionary. In the end return the new dictionary.
'''


def filterTheDict(dictObj, callback):
    newDict = {}
    # Iterate over all the items in dictionary
    for (key, value) in dictObj.items():
        # Check if item satisfies the given condition then add to new dict
        if callback((key, value)):
            newDict[key] = value
    return newDict


d_file = open('dictionary_compact.json')
dict = json.load(d_file)
print(len(dict))
game_dict = filterTheDict(dict, lambda elem: len(elem[0]) == 5)
print(len(game_dict))
print(random.choice(list(game_dict)))

def new_game():
  word = random.choice(list(game_dict))
  return {
    'word': word,
    'tries': 5,
    'letters': {}
  }

def play(word_try, game_state):
  word = game_state['word']
  if game_state['tries'] == 0:
    return False
  
  if word == word_try:
    return True
  else:
    # We now need to give hints
    for idx in range(0, len(word)):
      if word[idx] in word_try:
        if word[idx] == word_try[idx]:
          game_state['letters'][word_try[idx]] = idx
        else:
          game_state['letters'][word[idx]] = -1
    game_state['tries'] -= 1
    return game_state