import os
from sqla_wrapper import SQLAlchemy


def dobi_bazo():
    return SQLAlchemy(os.getenv("DATABASE_URL", "sqlite:///podatkovna-baza.sqlite?check_same_thread=False"))


db = dobi_bazo()


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    avtor = db.Column(db.String)
    vsebina = db.Column(db.String)


db.create_all()