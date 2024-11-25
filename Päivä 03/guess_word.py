word = 'kuningas'

resolved_word = ['_'] * len(word)
#resolved_word = list('_' * len(word))

#while ''.join(resolved_word) != word:
while '_' in resolved_word:
    print(''.join(resolved_word))
    letter = input('Kirjain? ')
    # for index in range(len(word)):
    for index, word_letter in enumerate(word):
        if word_letter == letter.lower():
            resolved_word[index] = letter.lower()
print('Voitit!')