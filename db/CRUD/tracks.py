from sqlalchemy.orm import declarative_base
import datetime
Base = declarative_base()

from db.models import Track
from db.CRUD.genres import update_genre_list
from db.CRUD.edits import add_new_edit



def add_new_track(Session,
    file_path,
    name,
    user=None,
    comment=None,
    author=None,
    lyrics=None,
    links=None,
    genre=None
    ):
    session = Session()

    genres = update_genre_list(session, genre) if genre else []
    now = datetime.date.today()

    track = Track(
        # user = user,
        file_path = file_path,
        name = name,
        comment = comment,
        author = author,
        lyrics = lyrics,
        links = links,
        add_at = now,
        edit_at = now,
        genres = genres
    )

    add_new_edit(
        session=session,
        track=track,
        add_at=now,
        user=user,
        file_path=file_path,
        name=name,
        comment=comment,
        author=author,
        lyrics=lyrics,
        links=links,
        genres=genres)

    session.add(track)
    session.commit()
    return track