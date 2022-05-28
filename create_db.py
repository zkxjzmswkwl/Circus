import os
from models import db, User, Message

def do_it_dad(usernames=None):
    os.remove("dev.db")
    db.connect()
    db.create_tables([User, Message])

    if usernames is not None:
        for i in usernames:
            me = User.create(name=i)
            me.save()

    me = User.create(name="Carter")
    not_me = User.create(name="Kim Jong Un")
    not_me.save()
    me.save()

    m = Message.create(
        content="Hey Kim, can you stop doing that bad stuff? :100:",
        sent_to=not_me,
        sent_by=me
    )
    m.save()
