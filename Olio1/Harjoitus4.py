game = Guessword('kuningas')

while not game.is_resolved():
    print(game.hidden_word())
    letter = input('Kirjain? ')
    game.resolve_letter(letter)

print('Voitit!')