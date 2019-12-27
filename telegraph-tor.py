from torrequest import TorRequest
from constants import browsers
import random
from bs4 import BeautifulSoup
from peewee import *
from telegraph_models import Headline, db

db.connect()

def random_headers():
    return {'User-Agent': random.choice(browsers)}

tr = TorRequest(proxy_port=9050, ctrl_port=9051, password=None)
target_url = 'https://telegraph.co.uk'

r = tr.get(target_url, headers=random_headers())
s = BeautifulSoup(r.text, 'lxml')
anchors = s.findAll('a', {'class': 'list-headline__link'})
for i, a in enumerate(anchors):
    span = a.find('span', {'class': 'e-kicker'})
    if span != None:
        span.extract()

for i, a in enumerate(anchors):
    headline, created = Headline.get_or_create(text=a.text.strip(), href=a['href'].strip())

