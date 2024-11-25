# Harjoitus:
# Kirjoita skripti, joka:
# - kysyy käyttäältä nimi ja ikä
# - printaa lause, jossa käytetään niitä

nimi = input('Kirjoita nimesi: ')
ikä = int(input('Kirjoita ikäsi: '))

# print('Moi', nimi, '. Olet', ikä, 'vuotta vanha')
# print('Moi ' + nimi + '. Olet ' + str(ikä) + ' vuotta vanha')
print(f'Moi {nimi}. Olet {ikä} vuotta vanha')


# Printaa lause, jossa kerrotan käyttäjälle minä vuonna se on syntynyt.

vuosi = 2024 - ikä
print(f'Olet syntynyt vuonna {vuosi}.')
