import os
from peewee import *

script_dir = os.path.dirname(__file__)
ap = os.path.join(script_dir, 'telegraph.db')
db = SqliteDatabase(ap)


class Headline(Model):
    text = CharField()
    href = CharField()

    class Meta:
        database = db
