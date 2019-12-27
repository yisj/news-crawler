from peewee import *

db = SqliteDatabase('telegraph.db')

class Headline(Model):
    text = CharField()
    href = CharField()

    class Meta:
        database = db

db.connect()
db.create_tables([Headline])
