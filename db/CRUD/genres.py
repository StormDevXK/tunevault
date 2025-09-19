from sqlalchemy.orm import declarative_base
import datetime
Base = declarative_base()

from db.models import Genre



def update_genre_list(session, genre_names):
    genres = []

    for name in genre_names:
        genre = session.query(Genre).filter_by(genre_name=name).first()
        if not genre:
            # если такого жанра нет — создаём новый
            genre = Genre(genre_name=name)
            session.add(genre)
            session.flush()
        genres.append(genre)

    return genres