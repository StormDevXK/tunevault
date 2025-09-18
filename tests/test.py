from sqlalchemy import create_engine, Column, Integer, String, Text, Date, DateTime, Enum, ForeignKey, Table
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
import datetime

Base = declarative_base()

# =========================
# Связующие таблицы Many-to-Many
# =========================
track_genres_table = Table(
    "track_genres",
    Base.metadata,
    Column("track_id", Integer, ForeignKey("tracks.id"), primary_key=True),
    Column("genre_id", Integer, ForeignKey("genres.id"), primary_key=True)
)

edit_genres_table = Table(
    "edit_genres",
    Base.metadata,
    Column("edit_id", Integer, ForeignKey("edits.id"), primary_key=True),
    Column("genre_id", Integer, ForeignKey("genres.id"), primary_key=True)
)

# =========================
# Users
# =========================
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    tracks = relationship("Track", back_populates="user")
    edits = relationship("Edit", back_populates="user")
    reactions = relationship("Reaction", back_populates="user")

# =========================
# Genres
# =========================
class Genre(Base):
    __tablename__ = "genres"

    id = Column(Integer, primary_key=True)
    genre_name = Column(String, nullable=False)

    tracks = relationship("Track", secondary=track_genres_table, back_populates="genres")
    edits = relationship("Edit", secondary=edit_genres_table, back_populates="genres")

# =========================
# Tracks
# =========================
class Track(Base):
    __tablename__ = "tracks"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    edit_at = Column(Date)
    add_at = Column(Date)

    name = Column(String)
    author = Column(String)
    comment = Column(Text)
    lyrics = Column(Text)
    links = Column(Text)
    file_path = Column(Text)

    user = relationship("User", back_populates="tracks")
    edits = relationship("Edit", back_populates="track")
    reactions = relationship("Reaction", back_populates="track")
    genres = relationship("Genre", secondary=track_genres_table, back_populates="tracks")

# =========================
# Edits
# =========================
class Edit(Base):
    __tablename__ = "edits"

    id = Column(Integer, primary_key=True)
    track_id = Column(Integer, ForeignKey("tracks.id"))
    user_id = Column(Integer, ForeignKey("users.id"))

    edit_at = Column(Date)

    name = Column(String)
    author = Column(String)
    comment = Column(Text)
    lyrics = Column(Text)
    links = Column(Text)
    file_path = Column(Text)

    track = relationship("Track", back_populates="edits")
    user = relationship("User", back_populates="edits")
    genres = relationship("Genre", secondary=edit_genres_table, back_populates="edits")

# =========================
# Reactions
# =========================
class Reaction(Base):
    __tablename__ = "reactions"

    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    track_id = Column(Integer, ForeignKey("tracks.id"), primary_key=True)
    type = Column(Enum("like", "dislike", "blacklist", name="reaction_type"))

    user = relationship("User", back_populates="reactions")
    track = relationship("Track", back_populates="reactions")

# =========================
# Создание базы
# =========================
if __name__ == "__main__":
    engine = create_engine("sqlite:///tests/music.db", echo=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Создадим данные
    user1 = User(username="Лизок228")
    user2 = User(username="Колька")
    rap = Genre(genre_name="Реп")
    jazz = Genre(genre_name="Джаз")

    track = Track(
        user=user1,
        name="XXXL",
        author="Монеточка",
        add_at=datetime.date.today(),
        genres=[rap, jazz]  # трек с несколькими жанрами
    )

    edit = Edit(
        track=track,
        user=user2,
        author="5opka",
        edit_at=datetime.date.today(),
        genres=[rap]  # редактирование с жанром Rock
    )

    session.add_all([
        user1, user2,
        rap, jazz,
        track, edit
        ])

    session.commit()
