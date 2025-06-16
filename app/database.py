from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Database URL
URL_DB = 'postgresql://postgres:Jio%403264@localhost:5432/rb_db'

# SQLAlchemy Engine & Session
engine = create_engine(URL_DB)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declarative Base
Base = declarative_base()
