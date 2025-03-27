import sys
import requests
from bs4 import BeautifulSoup

res = requests.get('https://taitotalo.fi')

if not res.ok:
    sys.exit(1)

html_doc = res.text
soup = BeautifulSoup(html_doc, 'html.parser')

# soup.h1
# soup.p
# link = soup.a
# link.span
# link['class']
# link['href']
# link.text
# link.string
# link.span.string
# link.next
# link.next.next
# link.next_sibling


