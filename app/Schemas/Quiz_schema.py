
from pydantic import BaseModel
from typing import List, Annotated



class ChoiceBase(BaseModel):
    choice_txt : str
    is_correct : bool
class QuestionBase(BaseModel):
    question_txt : str
    choice : List[ChoiceBase]