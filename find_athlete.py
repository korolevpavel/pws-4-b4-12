from sqlalchemy.orm import sessionmaker
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
import sys
from datetime import datetime

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
    
    return user_id

def find_bd(user, session):
    
    all_athletes = session.query(Athelete).all()
    id_athletes = {}

    for athlete in all_athletes:
        birthday = str_to_date(athlete.birthdate)
        id_athletes[athlete.id] = birthday

    user_birthday = str_to_date(user.birthdate)
    nearest = ""
    athlete_id = ""
    athlete_birthday = ""

    for id_athlete, birthday_athlete in id_athletes.items():
        nearest_abs = abs(user_birthday - birthday_athlete)
        if not nearest or nearest_abs < nearest:
            nearest =nearest_abs
            athlete_id = id_athlete
            athlete_birthday = birthday_athlete
    return athlete_id, athlete_birthday

def find_height(user, session):
     
    all_athletes = session.query(Athelete).all()
    id_athletes = {}

    for athlete in all_athletes:
        if athlete.height:
            id_athletes[athlete.id] = athlete.height

    user_heigth = user.height
    nearest = ""
    athlete_id = ""
    athlete_heigth = ""

    for id_athlete, heigth_athlete in id_athletes.items():
        
        if heigth_athlete is None:
            continue
        
        nearest_abs = abs(user_heigth - heigth_athlete)
        if not nearest or nearest_abs < nearest:
            nearest =nearest_abs
            athlete_id = id_athlete
            athlete_heigth = heigth_athlete

    return athlete_id, athlete_heigth

def str_to_date(date_str):

    date_test = date_str.replace("-", " ")
    datetime_object = datetime.strptime(date_test, "%Y %m %d")
   
    return datetime_object.date()

def main():

    session = connect_db()
    
    user_id = request_data()
    user = session.query(User).filter(User.id == user_id).first()

    if not user:
        print("Пользователь не найден в базе данных")
    else:
        athlete_id_birthday, athlete_birthday = find_bd(user, session)
        print("Ближайший атлет по дате рождения: {} родился: {}".format(athlete_id_birthday, athlete_birthday))
        athlete_id_height, athlete_heigth = find_height(user, session)
        print("Ближайший атлет по весу: {} родился: {}".format(athlete_id_height, athlete_heigth))

if __name__ == "__main__":
    main()