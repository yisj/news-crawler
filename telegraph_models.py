import os
from peewee import *

script_dir = os.path.dirname(__file__)
ap = os.path.join(script_dir, 'telegraph.db')
db = SqliteDatabase(ap)


class BaseModel(Model):
    class Meta:
        database = db

class Headline(BaseModel):
    text = TextField()
    href = TextField()
    crawl_try = IntegerField(default=0)
    crawl_success = IntegerField(default=0)

class Paragraph(BaseModel):
    text = TextField()
    headline = ForeignKeyField(Headline, backref='articles')

