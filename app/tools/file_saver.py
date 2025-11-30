# app/tools/file_saver.py
import os
from datetime import datetime
import pathlib

OUTPUT_DIR = os.path.join(os.getcwd(), "outputs")
pathlib.Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)

def save_markdown(content: str, session_id: str) -> str:
    ts = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    filename = f"blog_{session_id[:8]}_{ts}.md"
    path = os.path.join(OUTPUT_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return path
