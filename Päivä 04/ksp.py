#import random
#import random as rnd
from random import choice


OPTIONS = ('kivi', 'sakset', 'paperi')
OPTIONS_QUIT = ('quit', 'stop', 'end', 'q', 'x')

def get_player_option():
    while True:
        player_option = input('Kivi, sakset vai paperi? ')

        for option in OPTIONS:
            if player_option == option[0]:
                return option

        if player_option in OPTIONS:
            return player_option

        if player_option in OPTIONS_QUIT:
            return None

def get_winner_msg(player_option, computer_option):
    player_index = OPTIONS.index(player_option)
    computer_index = OPTIONS.index(computer_option)

    if player_index == computer_index:
        return 'Tasapeli!'
    elif computer_index == (player_index + 1) % 3:
        return 'Voitit!'
    else:
        return 'Kone voitti!'


while True:
    # Saada käyttäjän valinta
    player_option = get_player_option()
    if player_option is None:
        break
    
    # Saada koneen valinta
    computer_option = choice(OPTIONS)
    print(f'Kone valitse "{computer_option}"')

    # Laskea voittaja niiden perustella
    print(get_winner_msg(player_option, computer_option))

print('Kiitos pelaamisesta')