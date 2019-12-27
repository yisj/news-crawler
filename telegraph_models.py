import os
from peewee import *

ap = os.path.abspath('telegraph.db')
db = SqliteDatabase(ap)


class Headline(Model):
    text = CharField()
    href = CharField()

    class Meta:
        database = db
