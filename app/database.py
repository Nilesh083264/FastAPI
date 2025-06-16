from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

print("database.py")
# Database URL
URL_DB = 'postgresql://postgres:Jio%403264@localhost:5432/rb_db'

# SQLAlchemy Engine & Session
engine = create_engine(URL_DB)


# Declarative Base

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()