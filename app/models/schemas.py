from pydantic import BaseModel
from typing import Dict, List, Optional

class GradeRequest(BaseModel):
    answers: Dict[str, str]
    correct_answers: Dict[str, str]

class FileUploadResponse(BaseModel):
    filename: str
    batch_id: str
    query_url: str

class BatchResultItem(BaseModel):
    file_name: str
    state: str
    full_zip_url: str
    err_msg: str
    extracted_pages: int
    total_pages: int

class BatchResultResponse(BaseModel):
    batch_id: str
    results: List[BatchResultItem]