from sqlalchemy import create_engine, Column, Integer, String, Text, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
import time
import sqlalchemy.exc

Base = declarative_base()

class Story(Base):
    __tablename__ = 'stories'
    id = Column(Integer, primary_key=True)
    hn_id = Column(Integer, unique=True, nullable=False)
    title = Column(String(512))
    url = Column(String(1024))
    content = Column(Text)
    summary = Column(Text)

# Use environment variables or default values for DB connection
DB_USER = os.getenv('POSTGRES_USER', 'postgres')
DB_PASSWORD = os.getenv('POSTGRES_PASSWORD', 'postgres')
DB_HOST = os.getenv('POSTGRES_HOST', 'db')
DB_PORT = os.getenv('POSTGRES_PORT', '5432')
DB_NAME = os.getenv('POSTGRES_DB', 'postgres')

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def wait_for_db(engine, retries=10, delay=2):
    for i in range(retries):
        try:
            with engine.connect() as conn:
                conn.execute(text("SELECT 1"))
            return True
        except sqlalchemy.exc.OperationalError:
            print(f"Waiting for database... ({i+1}/{retries})")
            time.sleep(delay)
    raise Exception("Database not available after waiting.")

def init_db():
    wait_for_db(engine)
    Base.metadata.create_all(bind=engine)
