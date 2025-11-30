# app/models/schemas.py
from pydantic import BaseModel
from typing import Optional, Dict, Any

class GenerateRequest(BaseModel):
    topic: str
    tone: Optional[str] = "informative"
    length: Optional[str] = "short"

class SessionStatus(BaseModel):
    session_id: str
    status: str
    detail: Optional[Dict[str, Any]] = None

    class Config:
        extra = "allow"   # important

class ResultResponse(BaseModel):
    session_id: str
    path: Optional[str] = None
    snippet: Optional[str] = None

    class Config:
        extra = "allow"   # VERY IMPORTANT
