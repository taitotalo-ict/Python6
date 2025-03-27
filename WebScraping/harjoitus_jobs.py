import sys
import requests
from bs4 import BeautifulSoup

url = 'https://realpython.github.io/fake-jobs/'
res = requests.get(url, timeout=10)
if not res.ok:
    sys.exit(1)

soup = BeautifulSoup(res.text, 'html.parser')

counter = 0
for card in soup.find_all(class_='card'):
    location = card.find('p', class_='location').text.strip()
    state = location.split(',')[1].strip()
    if state != 'AE':
        continue
    counter += 1
    title = card.h2.text.strip()
    link = card.find('a', string='Apply')['href']

    print(f'Työtarjous {counter}: {title}\nSijainti: {location}\nLinkki: {link}\n')

    