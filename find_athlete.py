from sqlalchemy.orm import sessionmaker
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
import sys
import datetime

DB_PATH = "sqlite:///" + sys.argv[1]
Base = declarative_base()

class User(Base):

    __tablename__ = "user"

    id = sa.Column(sa.INTEGER, primary_key=True) 
    first_name = sa.Column(sa.TEXT)
    last_name = sa.Column(sa.TEXT)
    gender = sa.Column(sa.TEXT)
    email = sa.Column(sa.TEXT)
    birthdate = sa.Column(sa.TEXT)
    height = sa.Column(sa.FLOAT)

class Athelete(Base):

    __tablename__ = "athelete"

    id = sa.Column(sa.INTEGER, primary_key=True) 
    age = sa.Column(sa.INTEGER)
    birthdate = sa.Column(sa.TEXT)
    gender = sa.Column(sa.TEXT)
    height = sa.Column(sa.FLOAT)
    name = sa.Column(sa.TEXT)
    weight = sa.Column(sa.INTEGER)
    gold_medals = sa.Column(sa.INTEGER)
    silver_medals = sa.Column(sa.INTEGER)
    bronze_medals = sa.Column(sa.INTEGER)
    total_medals = sa.Column(sa.INTEGER)
    sport = sa.Column(sa.TEXT)
    country = sa.Column(sa.TEXT)

def connect_db():

    engine = sa.create_engine(DB_PATH)
    Sessions = sessionmaker(engine)
    session = Sessions()
    return session

def request_data():

    print("Поиск атлетов")
    user_id = input("Введите идентификатор пользователя: ")
    
    return user

def main():

    session = connect_db()
    new_user = request_data()
    session.add(new_user)
    session.commit()

    print("Пользователь зарегистрирован!")

if __name__ == "__main__":
    main()