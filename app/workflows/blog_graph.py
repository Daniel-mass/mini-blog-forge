# app/workflows/blog_graph.py
"""
Simple sequential orchestrator implementation.
We keep it simple: orchestrate three agents in sequence and provide status updates.
"""

from app.agents.research_agent import ResearchAgent
from app.agents.outline_agent import OutlineAgent
from app.agents.draft_agent import DraftAgent
from app.tools.file_saver import save_markdown
import logging
import uuid

class MiniBlogFlow:
    def __init__(self):
        self.research = ResearchAgent()
        self.outliner = OutlineAgent()
        self.drafter = DraftAgent()

    def run(self, topic: str, tone: str = "informative", length: str = "short", session_meta: dict = None) -> dict:
        """
        Runs the three agents and saves output to a file.
        Returns a dict with status, path, and snippet.
        """
        session_meta = session_meta or {}
        sid = session_meta.get("session_id", str(uuid.uuid4()))
        logging.info(f"MiniBlogFlow: start session {sid}")

        # step 1: research
        logging.info("MiniBlogFlow: research step")
        brief = self.research.run(topic)

        # step 2: outline
        logging.info("MiniBlogFlow: outline step")
        outline = self.outliner.run(brief, topic)

        # step 3: draft
        logging.info("MiniBlogFlow: draft step")
        draft = self.drafter.run(outline, brief, topic, tone=tone, length=length)

        # save
        path = save_markdown(draft, sid)
        logging.info(f"MiniBlogFlow: saved draft to {path}")

        snippet = "\n".join(draft.splitlines()[:8])
        return {"session_id": sid, "path": path, "snippet": snippet, "status": "completed"}
