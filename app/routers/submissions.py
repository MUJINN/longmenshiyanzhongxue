from fastapi import APIRouter, HTTPException
from app.models.schemas import GradeRequest
from app.services.grading_service import grade_submission

router = APIRouter(prefix="/submissions", tags=["自动批改"])

@router.post("/grade")
async def grade_submission_api(request: GradeRequest):
    try:
        result = grade_submission(request.answers, request.correct_answers)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))