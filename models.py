import uuid
import datetime

from peewee import SqliteDatabase, Model, TextField, DateField, IntegerField, UUIDField, ForeignKeyField

db = SqliteDatabase("dev.db")


class BobbyLee(Model):
    class Meta:
        database = db


class User(BobbyLee):
    id = UUIDField(primary_key=True, default=uuid.uuid4)
    name = TextField(null=False, index=True)
    time_stamp = DateField(default=datetime.datetime.now)


class Message(BobbyLee):
    content = TextField()
    time_stamp = DateField(default=datetime.datetime.now)
    sent_by = ForeignKeyField(User, backref="messages")
    sent_to = ForeignKeyField(User, backref="messages")
