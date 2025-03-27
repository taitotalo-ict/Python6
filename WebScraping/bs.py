import requests
import sys

res = requests.get('https://taitotalo.fi')

if not res.ok:
    sys.exit(1)

print(res.text)