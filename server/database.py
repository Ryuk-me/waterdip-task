from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from server.Config import configs
from sqlalchemy_utils import database_exists, create_database

SQLALCHEMY_DATABASE_URL = f"postgresql://{configs.DATABASE_USERNAME}:{configs.DATABASE_PASSWORD}@{configs.DATABASE_HOSTNAME}:{configs.DATABASE_PORT}/{configs.DATABASE_NAME}"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

if not database_exists(engine.url):
    create_database(engine.url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def is_db_connected():
    try:
        get_db()
        return True
    except:
        return False
