import uuid
import datetime

from peewee import SqliteDatabase, Model, TextField, DateField, IntegerField, UUIDField, ForeignKeyField

db = SqliteDatabase("dev.db")


class BobbyLee(Model):
    """
    If we don't do this here, each table class (User, Message, etc)
    will need the same
        class Meta:
            database = db
    boilerplate.
    """
    class Meta:
        database = db


class User(BobbyLee):
    id = UUIDField(primary_key=True, default=uuid.uuid4)
    name = TextField(null=False, index=True)
    time_stamp = DateField(default=datetime.datetime.now)


class MessageFork(BobbyLee):
    """
    A fork in each message's road.
    Is it going to a server, or is it going to a single person (direct message)?
    Waiting on implementing this until *a* base client implementation is capable of sending messages.
    Gives my slow silly brain time to process the super duper important decision.
    """
    id = UUIDField(primary_key=True, default=uuid.uuid4)
    time_stamp = DateField(default=datetime.datetime.now)


class Message(BobbyLee):
    id = UUIDField(primary_key=True, defualt=uuid.uuid4)
    content = TextField()
    time_stamp = DateField(default=datetime.datetime.now)
    sent_by = ForeignKeyField(User, backref="messages")
    sent_to = ForeignKeyField(User, backref="messages")


class Server(BobbyLee):
    """
    Waiting on implementing this until *a* base client implementation is capable of sending messages.
    Gives my slow silly brain time to process the super duper important decision.
    """
    id = UUIDField(primary_key=True, defualt=uuid.uuid4)
    name = TextField()
    icon = TextField()
