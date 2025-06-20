from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base,engine





print("In models.py")
class Questions(Base):
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True, index=True)
    question_txt = Column(String, index=True)

    # One-to-many relationship: one question has many choices
    choices = relationship("Choices", back_populates="question", cascade="all, delete-orphan")


class Choices(Base):
    __tablename__ = "choices"

    id = Column(Integer, primary_key=True, index=True)
    choice_txt = Column(String, index=True)
    is_correct = Column(Boolean, default=False)

    question_id = Column(Integer, ForeignKey("questions.id"))

    # Relationship to parent question
    question = relationship("Questions", back_populates="choices")



Base.metadata.create_all(bind=engine)
