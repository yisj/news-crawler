from peewee import *
from telegraph_models import db, Headline

db.connect()
db.create_tables([Headline])
