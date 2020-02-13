from torrequest import TorRequest
from constants import browsers
import random
from bs4 import BeautifulSoup
from peewee import *
from telegraph_models import Headline, Paragraph, db

db.connect()

def random_headers():
    return {'User-Agent': random.choice(browsers)}

tr = TorRequest(proxy_port=9052, ctrl_port=9053, password=None)


headlines = Headline.select()

for headline in headlines:
    if headline.crawl_success == 0 and headline.crawl_try == 0:

        try:
            if 'https://www.telegraph.co.uk' in headline.href:
                href = headline.href
            else:
                href = 'https://www.telegraph.co.uk' + headline.href
            print(href, 'need to be crawled')
            r = tr.get(href, headers=random_headers())
            headline.crawl_try += 1
            headline.save()
        
            s = BeautifulSoup(r.text, 'lxml')
            main = s.find('main', {'class': ['row', 'article__body']})
            abody = main.find('article')
            body = abody.find('div', {'class': 'component-content'})
            ps = body.findAll('p')
            for p in ps:
                Paragraph.get_or_create(text=p.text.strip(), headline=headline)
        
            headline.crawl_success += 1
            headline.save()
        except:
            pass


