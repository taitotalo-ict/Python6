#import random
#import random as rnd
from random import choice


OPTIONS = ('kivi', 'sakset', 'paperi')
OPTIONS_QUIT = ('quit', 'stop', 'end', 'q', 'x')


while True:
    # Saada käyttäjän valinta
    while True:
        player_option = input('Kivi, sakset vai paperi? ')

        # if player_option == 'k':
        #     player_option = 'kivi'
        #     break
        # if player_option == 's':
        #     player_option = 'sakset'
        #     break
        # if player_option == 'p':
        #     player_option = 'paperi'
        #     break

        for option in OPTIONS:
            if player_option == option[0]:
                player_option = option

        if player_option in OPTIONS:
            break

        if player_option in OPTIONS_QUIT:
            player_option = None
            break
    
    if player_option is None:
        break
    
    # Saada koneen valinta
    computer_option = choice(OPTIONS)
    print(f'Kone valitse "{computer_option}"')

    # Laskea voittaja niiden perustella
    player_index = OPTIONS.index(player_option)
    computer_index = OPTIONS.index(computer_option)

    if player_index == computer_index:
        print('Tasapeli!')
    elif computer_index == (player_index + 1) % 3:
        print('Voitit!')
    else:
        print('Kone voitti!')

    # if computer_option == player_option:
    #     print('Tasapeli!')
    # # elif player_option == 'kivi':
    # #     if computer_option == 'sakset':
    # #         print('Voitit!')
    # #     else:
    # #         print('Kone voitti!')
    # # elif player_option == 'sakset':
    # #     if computer_option == 'paperi':
    # #         print('Voitit!')
    # #     else:
    # #         print('Kone voitti!')
    # # else:
    # #     if computer_option == 'kivi':
    # #         print('Voitit!')
    # #     else:
    # #         print('Kone voitti!')
    # elif (player_option == 'kivi' and computer_option == 'sakset') \
    #    or (player_option == 'sakset' and computer_option == 'paperi') \
    #    or (player_option == 'paperi' and computer_option == 'kivi'):
    #     print('Voitit!')
    # else:
    #     print('Kone voitti!')

print('Kiitos pelaamisesta')