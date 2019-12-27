from peewee import *
from telegraph_models import db, Headline, Article

db.connect()
db.create_tables([Headline, Article])
