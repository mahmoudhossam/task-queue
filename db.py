from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String, Integer
from sqlalchemy_utils import database_exists, create_database

Base = declarative_base()


class DB:
    def __init__(self):
        """This connects to the database and sets up the session."""
        self.engine = create_engine("postgresql://user:password@postgres:5432/users")
        session_maker = sessionmaker(bind=self.engine)
        self.session = session_maker()

    def add(self, user):
        """This does an upsert in case of existing email, a regular insert if not."""
        existing_user = (
            self.session.query(User).filter(User.email == user.email).first()
        )
        if existing_user:
            existing_user.name = user.name
            self.session.add(existing_user)
        else:
            self.session.add(user)
        self.session.commit()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(50), unique=True)


if __name__ == "__main__":
    """This creates the database if it does not exist."""
    db = DB()
    if not database_exists(db.engine.url):
        create_database(db.engine.url)
    Base.metadata.create_all(db.engine)
