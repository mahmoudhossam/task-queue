from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String, Integer
from sqlalchemy_utils import database_exists, create_database

Base = declarative_base()


class DB:
    def __init__(self):
        self.engine = create_engine("postgresql://user:password@postgres:5432/users")
        session_maker = sessionmaker(bind=self.engine)
        self.session = session_maker()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(50))


if __name__ == "__main__":
    db = DB()
    if not database_exists(db.engine.url):
        create_database(db.engine.url)
    Base.metadata.create_all(db.engine)
