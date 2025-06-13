from fastapi import APIRouter
from api.controller.HandleLogicController import router as handle_logic

router = APIRouter()
router.include_router(handle_logic)