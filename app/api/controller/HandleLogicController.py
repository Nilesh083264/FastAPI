from fastapi import Request, APIRouter, Depends
from services.endpoint_extractors import CommandFactory
from sqlalchemy.orm import Session
from database import get_db
router = APIRouter()

@router.get("/")
def hello_world():
    return "Hello World"


@router.post("/URLS")
async def Data_Requests (requests: Request):
    try:
        data = await requests.json()
        cmd = CommandFactory.get_command(data["Endpoint"])
        if cmd:
            cmd.execute(data["Payload"])
        else:
            print("Invalid action:", data["Endpoint"])

    except Exception as e:
        print(str(e))

@router.get("/test-db")
def test_db_connection(db: Session = Depends(get_db)):
    result = db.execute("SELECT 1")
    return {"status": "Connected", "result": list(result)}