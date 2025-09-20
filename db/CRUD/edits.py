from sqlalchemy.orm import declarative_base
import datetime
Base = declarative_base()

from ..models import Edit
from db.CRUD.genres import update_genre_list



def add_new_edit(
    session,
    track=None,
    add_at=None,
    user=None,
    file_path=None,
    name=None,
    comment=None,
    author=None,
    lyrics=None,
    links=None,
    genres=None
    ):
    
    edit = Edit(
        track = track,
        # user = user,
        file_path = file_path,
        name = name,
        comment = comment,
        author = author,
        lyrics = lyrics,
        links = links,
        edit_at = datetime.date.today(),
        add_at = add_at,
        genres = genres
    )

    session.add(edit)
    session.flush()

    return edit



