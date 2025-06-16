from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import JSONResponse
from services.endpoint_extractors import CommandFactory
from core.db_session import db_dependency
from models import Questions, Choices
from typing import Dict
from Schemas.Quiz_schema import ChoiceBase,QuestionBase
router = APIRouter()


@router.get("/")
def hello_world():
    return {"message": "Hello World"}

@router.post("/URLS")
async def data_requests(requests: Request):
    try:
        data = await requests.json()
        cmd = CommandFactory.get_command(data.get("Endpoint"))
        if cmd:
            cmd.execute(data.get("Payload"))
            return JSONResponse(content={"status": "success", "message": "Command executed"})
        else:
            return JSONResponse(status_code=400, content={"status": "error", "message": "Invalid endpoint"})
    except Exception as e:
        return JSONResponse(status_code=500, content={"status": "error", "message": str(e)})


@router.post("/questions/")
async def create_questions(question : QuestionBase, db:db_dependency):
    db_question = Questions(question_txt = question.question_txt)
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    for choice in question.choice:
        db_choice = Choices(
            choice_txt=choice.choice_txt,
            is_correct=choice.is_correct,
            question_id=db_question.id
        )
        db.add(db_choice)

    db.commit()
    return {"message": "Question and choices created successfully"}


@router.get("/que/{QID}")
def read_question(QID:int, db:db_dependency):
    Que= db.query(Questions).filter(Questions.id == QID).all()
    opts = db.query(Choices).filter(Choices.question_id == QID).all()
    correct_ans = db.query(Choices).filter(Choices.is_correct == True, Choices.question_id == QID).all()
    output = {
        "Question " : Que,
        "Choices" : opts,
        "Answer" : correct_ans
    }
    if not output:
        raise HTTPException(status_code=404,detail="QID not Found")
    return output


