from sqlalchemy import create_engine, Column, Integer, String, Text, Date, DateTime, Enum, ForeignKey, Table
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
import datetime

from CRUD import add_new_track, get_genre_list

Base = declarative_base()

if __name__ == "__main__":
    engine = create_engine("sqlite:///tests/music.db", echo=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    # user_id = 1
    file_path = '123'

    name = input('name')
    comment = input('comment')
    author = input('author')
    lyrics = input('lyrics')
    links= input('links')

    genre = []
    genre.append(input('genre'))

    add_new_track(Session, file_path, name, comment, author, lyrics, links, genre)


    # print("-------------", get_genre_list(Session, ["Реп", "Фонк"]))




    
    


