from random import shuffle, randint

def play(verbose:bool, change:bool = True) -> bool:
    options = ['Goat', 'Goat', 'Car']
    shuffle(options)

    # Pelaajan valinta
    player_option = randint(0, 2)
    if verbose:
        print(f'Pelaaja valitse ovi {player_option+1}')
    
    # Montyn valinta
    monty_option = (player_option + 1) % 3
    if options[monty_option] == 'Car':
        monty_option = (monty_option + 1) % 3
    if verbose:
        print(f'Monty näyttää ovea {monty_option+1}, jossa on {options[monty_option]}')

    # Pelaajan ratkaisu
    if verbose:
        print(f'Jos pelaaja ei vaihta ovea, se saisi {options[player_option]}')
    
    if change:
        player_option = 3 - player_option - monty_option
        if verbose:
            print(f'Jos pelaaja vaihtaa oveen {player_option+1}, se saisi {options[player_option]}')

    return options[player_option] == 'Car'

if __name__ == '__main__':
    # play(verbose=True)
    wins = 0
    rounds = 1000000
    for _ in range(rounds):
        if play(verbose=False, change=True):
            wins += 1

    print(f'Pelaaja on voitanut {wins/rounds * 100}% kertaa')