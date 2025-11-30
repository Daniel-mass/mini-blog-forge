# app/main.py
import uvicorn
import logging
from fastapi import FastAPI, HTTPException
from app.models.schemas import GenerateRequest, SessionStatus, ResultResponse
from app.workflows.blog_graph import MiniBlogFlow
import threading
import time

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

app = FastAPI(title="MiniBlogForge API")
flow = MiniBlogFlow()

# simple in-memory session store
SESSIONS = {}

@app.post("/generate", response_model=SessionStatus)
def generate(payload: GenerateRequest):
    session_id = payload.topic[:8].replace(" ", "_") + "_" + str(int(time.time()))
    SESSIONS[session_id] = {"status": "queued", "detail": None}

    def job():
        try:
            SESSIONS[session_id]["status"] = "running"
            result = flow.run(payload.topic, tone=payload.tone, length=payload.length, session_meta={"session_id": session_id})
            SESSIONS[session_id]["status"] = "completed"
            SESSIONS[session_id]["detail"] = result
        except Exception as e:
            logging.exception("Job failed")
            SESSIONS[session_id]["status"] = "failed"
            SESSIONS[session_id]["detail"] = {"error": str(e)}

    thread = threading.Thread(target=job, daemon=True)
    thread.start()

    return {"session_id": session_id, "status": "queued", "detail": None}

@app.get("/status/{session_id}", response_model=SessionStatus)
def status(session_id: str):
    sess = SESSIONS.get(session_id)
    if not sess:
        raise HTTPException(status_code=404, detail="Session not found")
    return {"session_id": session_id, "status": sess["status"], "detail": sess.get("detail")}

@app.get("/result/{session_id}", response_model=ResultResponse)
def result(session_id: str):
    sess = SESSIONS.get(session_id)
    if not sess:
        raise HTTPException(status_code=404, detail="Session not found")

    if sess["status"] != "completed":
        raise HTTPException(
            status_code=400,
            detail=f"Session not completed. Current status: {sess['status']}"
        )

    d = sess["detail"]
    path = d.get("path")

    if not path or not path.strip():
        raise HTTPException(status_code=500, detail="Output file path missing")

    # Read file content
    try:
        with open(path, "r", encoding="utf-8") as f:
            full_content = f.read()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to read output file: {str(e)}")

    return {
        "session_id": session_id,
        "path": path,
        "content": full_content  # FULL BLOG, NOT SNIPPET
    }
