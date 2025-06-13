from sqlalchemy.orm import Session
from core.DB_config import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
