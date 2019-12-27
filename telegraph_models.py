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

class Article(BaseModel):
    title = TextField()
    body = TextField()
    headline = ForeignKeyField(Headline, backref='articles')

