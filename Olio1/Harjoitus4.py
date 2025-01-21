class Guessword:
    def __init__(self, word: str) -> None:
        self._word = word
        self._resolved_word = ['_'] * len(word)

    def is_resolved(self) -> bool:
        return '_' not in self._resolved_word

    def hidden_word(self) -> str:
        return ''.join(self._resolved_word)
    
    def resolve_letter(self, letter: str) -> None:
        for index, word_letter in enumerate(self._word):
            if word_letter == letter.lower():
                self._resolved_word[index] = letter.lower()

game = Guessword('kuningas')

while not game.is_resolved():
    print(game.hidden_word())
    letter = input('Kirjain? ')
    game.resolve_letter(letter)

print('Voitit!')