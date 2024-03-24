from peewee import Model, CharField
from database.database import db

class Cliente(Model):
    nome = CharField()
    email = CharField()

    class Meta():
        database = db