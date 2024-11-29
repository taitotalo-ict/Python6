import random


OPTIONS = ('kivi', 'sakset', 'paperi')
OPTIONS_QUIT = ('quit', 'stop', 'end', 'q', 'x')


while True:
    # Saada käyttäjän valinta
    while True:
        player_option = input('Kivi, sakset vai paperi? ')
        if player_option in OPTIONS:
            break
        if player_option in OPTIONS_QUIT:
            player_option = None
            break
    
    if player_option is None:
        break
    
    # Saada koneen valinta
    computer_option = random.choice(OPTIONS)
    print(f'Kone valitse "{computer_option}"')

    # Laskea voittaja niiden perustella
    if computer_option == player_option:
        print('Tasapeli!')
    # elif player_option == 'kivi':
    #     if computer_option == 'sakset':
    #         print('Voitit!')
    #     else:
    #         print('Kone voitti!')
    # elif player_option == 'sakset':
    #     if computer_option == 'paperi':
    #         print('Voitit!')
    #     else:
    #         print('Kone voitti!')
    # else:
    #     if computer_option == 'kivi':
    #         print('Voitit!')
    #     else:
    #         print('Kone voitti!')
    elif (player_option == 'kivi' and computer_option == 'sakset') \
       or (player_option == 'sakset' and computer_option == 'paperi') \
       or (player_option == 'paperi' and computer_option == 'kivi'):
        print('Voitit!')
    else:
        print('Kone voitti!')

print('Kiitos pelaamisesta')