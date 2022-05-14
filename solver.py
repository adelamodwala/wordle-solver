import json
from wordle import new_game, play

d_file = open('dictionary_compact.json')
dict = json.load(d_file)

game_state = new_game()
game_state['word'] = 'liver'
print(game_state)
game_state = play("sleek", game_state)
print(game_state)
game_state = play("train", game_state)
print(game_state)