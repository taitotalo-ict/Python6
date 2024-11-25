# Kysy jostain numerosta
# Tarkista onko numeerinen vastaus
# Kysy uudelleen jos ei ole
# Muunna kokonaisluvuksi jos vastaus on num.

# While/For, input, int, if

is_not_number = True
while is_not_number:
    # Kysy
    vastaus = input('Ikä? ')
    if not vastaus: # Vastaus on tyhjä (käyttäjä on vain painanut Enteria)
        continue

    is_not_number = False
    # Tarkista
    for character in vastaus:
        # if character >= '0' and character <= '9':
        # if '0' <= character <= '9':
        if character not in '0123456789':
            is_not_number = True
            print('Vastaus ei ole numero')
            break

ikä = int(vastaus)
