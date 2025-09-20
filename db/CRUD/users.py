from sqlalchemy.orm import declarative_base
import datetime
Base = declarative_base()

from db.models import User



def add_new_user(Session, tg_id, username):
    session = Session()

    user = User(
        tg_id = tg_id,
        username = username
    )

    session.add(user)
    session.commit()


def create_user(session, username, tg_id=None):
    user = User(username=username, tg_id=tg_id)

    session.add(user)
    session.commit()

    return user