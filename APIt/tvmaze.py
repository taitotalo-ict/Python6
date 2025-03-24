import requests
from pprint import pprint

url = 'https://api.tvmaze.com'
res = requests.get(url+'/search/shows', params={'q': 'putous'})
if not res.ok:
    raise Exception

content = res.json()
id = content[0]['show']['id']

res = requests.get(url+f'/shows/{id}/episodes')
if not res.ok:
    raise Exception

# print(len(content))
# pprint(content[0])
for episode in res.json():
    season = episode['season']
    number = episode['number']
    airdate = episode['airdate']
    print(f'Season {season} - Episode {number} - {airdate}')
