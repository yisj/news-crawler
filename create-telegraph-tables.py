from peewee import *
from telegraph_models import db, Headline, Paragraph 

db.connect()
db.create_tables([Headline, Paragraph])
