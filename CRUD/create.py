from sqlalchemy import create_engine, Column, Integer, String, Text, Date, DateTime, Enum, ForeignKey, Table
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
import datetime
Base = declarative_base()

from CRUD import update
from setup_db import User, Genre, Track, Edit, Reaction  
from CRUD.update import update_genre_list



def add_new_user(Session, tg_id, username):
    session = Session()

    user = User(
        tg_id = tg_id,
        username = username
    )

    session.add(user)
    session.commit()



def add_new_track(Session, file_path, name, comment, author, lyrics, links, genre):
    session = Session()

    track = track_initialize(Session)
    genres = update_genre_list(Session, genre)

    edit = Edit(
        track = track,
        # user = None,
        file_path = file_path,
        name = name,
        comment = comment,
        author = author,
        lyrics = lyrics,
        links = links,
        edit_at = datetime.date.today(),
        genres = genres
    )

    session.add(edit)
    session.commit()



def track_initialize(Session):
    session = Session()

    track = Track()

    session.add(track)
    session.commit()

    return track



def add_user():
    pass






