from sqlalchemy import create_engine, Column, Integer, String, Text, Date, DateTime, Enum, ForeignKey, Table
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
import datetime
Base = declarative_base()

from setup_db import User, Genre, Track, Edit, Reaction  


def update_genre_list(Session, genre_names):
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




def track_update(track_id):
    pass
