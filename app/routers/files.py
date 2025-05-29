from fastapi import APIRouter, UploadFile, File, HTTPException
from pathlib import Path
from app.services.mineru_service import MinerUService
from app.models.schemas import FileUploadResponse
from app.utils import UPLOAD_DIR

router = APIRouter(prefix="/files", tags=["文件处理"])

mineru_service = MinerUService()

@router.post("/upload", response_model=FileUploadResponse)
async def upload_file(file: UploadFile = File(...)):
    allowed_types = {".pdf", ".jpg", ".jpeg", ".png", ".docx"}
    file_suffix = Path(file.filename).suffix.lower()

    if file_suffix not in allowed_types:
        raise HTTPException(status_code=400, detail=f"Unsupported file type: {file_suffix}")

    file_location = UPLOAD_DIR / file.filename

    try:
        with open(file_location, "wb+") as f:
            f.write(file.file.read())
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to save file: {str(e)}")

    try:
        batch_id, upload_url = mineru_service.apply_upload_url(file.filename)
        mineru_service.upload_file_to_mineru(file_location, upload_url)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return {
        "filename": file.filename,
        "batch_id": batch_id,
        "query_url": f"/files/results/{batch_id}"
    }

@router.get("/results/{batch_id}")
async def get_batch_result(batch_id: str):
    try:
        result = mineru_service.get_task_result(batch_id)
        extract_results = result.get("data", {}).get("extract_result", [])
        formatted_results = []
        for item in extract_results:
            formatted_results.append({
                "file_name": item.get("file_name"),
                "state": item.get("state"),
                "full_zip_url": item.get("full_zip_url"),
                "err_msg": item.get("err_msg"),
                "extracted_pages": item.get("extract_progress", {}).get("extracted_pages"),
                "total_pages": item.get("extract_progress", {}).get("total_pages")
            })
        return {"batch_id": batch_id, "results": formatted_results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))