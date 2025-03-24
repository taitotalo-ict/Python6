from pathlib import Path
import sys
from dotenv import dotenv_values
import requests


BASEDIR = Path(__file__).parent

config = dotenv_values(BASEDIR / ".env")
api_key = config['api_key']

url = 'https://api.nasa.gov/planetary/apod'
res = requests.get(
    url, 
    params = {'api_key': api_key, 'count': 10}, 
    timeout = 10,
)
if not res.ok:
    print(res.reason)
    sys.exit(1)

for resource in res.json():
    if resource['media_type'] != 'image':
        continue

    # Hoidetaan kuvan kansio
    year, month, _ = resource['date'].split('-')
    image_folder = Path(BASEDIR / 'images' / year / month)
    if not image_folder.exists():
        image_folder.mkdir(parents=True)
    
    # Saada kuvan polku
    image_url = resource['url']
    image_filename = image_folder / image_url.split('/')[-1]
    if image_filename.exists():
        continue

    # Ladataan kuvaa
    print(f'Ladataan {image_url}...')
    res = requests.get(image_url, timeout=10)
    if not res.ok:
        print(f'Virhe: Kuvaa osoitteessa {image_url} ei pysty latamaan.')
        continue
    
    # Tallenetaan kuvan tiedostoon
    with open(image_filename, 'wb') as f:
        f.write(res.content)

    # Kirjoitetaan tekstitiedosto
    text_filename = image_folder / (image_filename.stem + '.txt')
    with open(text_filename, 'w') as f:
        f.write(f'Title: {resource['title']}\n')
        f.write(f'Date: {resource['date']}\n')
        f.write(f'Explanation: {resource['explanation']}\n')