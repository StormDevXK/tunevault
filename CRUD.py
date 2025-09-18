from sqlalchemy import create_engine, Column, Integer, String, Text, Date, DateTime, Enum, ForeignKey, Table
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
import datetime
Base = declarative_base()

from setup_db import User, Genre, Track, Edit, Reaction  




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
    genres = get_genre_list(Session, genre)

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



def track_replace(track_id, edit_id, user_id):
    pass



def track_update(track_id):
    pass



def add_user():
    pass



def get_genre_list(Session, genre_names):
    session = Session()
    genres = []

    for name in genre_names:
        genre = session.query(Genre).filter_by(genre_name=name).first()
        if not genre:
            # если такого жанра нет — создаём новый
            genre = Genre(genre_name=name)
            session.add(genre)
            session.commit()
        genres.append(genre)

    return genres



