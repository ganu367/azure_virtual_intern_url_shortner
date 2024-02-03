from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import dotenv_values, load_dotenv
import os
import psycopg2

config = dotenv_values(".env")
connect = load_dotenv()

# defining postgres sql database
SQLALCHEMY_DATABASE_URL = os.getenv('SQLITE_URL')


# SQLALCHEMY_DATABASE_URL = 'postgresql+psycopg2://fastapiganu:brandly#1234@fastapi-database.postgres.database.azure.com/brandly_url?sslmode=require'

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL,connect_args={"check_same_thread": False}
# )

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
# getting database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
