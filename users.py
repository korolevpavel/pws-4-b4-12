from sqlalchemy.orm import sessionmaker
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
import sys

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

def connect_db():

    engine = sa.create_engine(DB_PATH)
    Sessions = sessionmaker(engine)
    session = Sessions()
    return session

def request_data():

    print("Добрый день! Сейчас произойдет регистрация пользователя в базе данных")
    first_name = input("Введите имя: ")
    last_name = input("Введите фамилию: ")
    gender = input("Укажите свой пол (Male - мужской, Female - женский): ")
    email = input("Введите адрес электронной почты: ")
    birthdate = input("Укажите дату рождения: ")
    height = input("Укажите свой рост: ")

    user = User(
        first_name = first_name,
        last_name = last_name,
        gender = gender,
        email = email,
        birthdate = birthdate,
        height = height
    )
    
    return user

def main():

    session = connect_db()
    new_user = request_data()
    session.add(new_user)
    session.commit()

    print("Пользователь зарегистрирован!")

if __name__ == "__main__":
    main()