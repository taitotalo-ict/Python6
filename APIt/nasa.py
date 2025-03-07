from pathlib import Path
from pprint import pprint
import requests
from dotenv import load_dotenv, dotenv_values
# import os

BASEDIR = Path(__file__).parent

# Option 1 (environment variables)
# load_dotenv()
# api_key = os.environ['api_key']

# Option 2 (config variable)
config = dotenv_values(BASEDIR / ".env")
api_key = config['api_key']
# api_key = dotenv_values(".env")['api_key']

url = 'https://api.nasa.gov/planetary/apod'
res = requests.get(url, params = {'api_key': api_key})
if not res.ok:
    print(res.reason)
    raise Exception
    

image_url = res.json()['url']
res = requests.get(image_url)
if not res.ok:
    print(res.reason)
    raise Exception

image_filename = BASEDIR / image_url.split('/')[-1]

with open(image_filename, 'wb') as f:
    f.write(res.content)
