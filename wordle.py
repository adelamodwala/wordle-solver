import json
import random

from sympy import true

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


def getRandomWord():
		return random.choice(list(game_dict))


def getGameDict():
		d_file = open('dictionary_compact.json')
		dict = json.load(d_file)
		print(len(dict))
		game_dict = filterTheDict(dict, lambda elem: len(elem[0]) == 5)
		return game_dict


game_dict = getGameDict()
print(len(game_dict))
print(random.choice(list(game_dict)))


def new_game():
		word = getRandomWord()
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
						letter = word[idx]
						guess_letter = word_try[idx]
						if guess_letter in word:
								if not guess_letter in game_state['letters']:
										game_state['letters'][guess_letter] = {
												'exists': True,
												'match_idx': set(),
												'mismatch_idx': set()
										}

								if letter == guess_letter:
										game_state['letters'][guess_letter]['match_idx'].add(idx)
								else:
										game_state['letters'][guess_letter]['mismatch_idx'].add(idx)
						else:
								game_state['letters'][guess_letter] = {'exists': False}
				game_state['tries'] -= 1
				return game_state
