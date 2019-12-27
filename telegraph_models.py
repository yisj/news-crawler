from peewee import *

db = SqliteDatabase('/home/seungjae/news-crawler/telegraph.db')

class Headline(Model):
    text = CharField()
    href = CharField()

    class Meta:
        database = db
