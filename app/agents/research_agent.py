# app/agents/research_agent.py
import logging
from app.utils.gemini_client import call_gemini, DEFAULT_MODEL


class ResearchAgent:
    """
    Produces a short research brief for a given topic.
    Acts as the first agent in the pipeline.
    """

    def __init__(self, model: str = DEFAULT_MODEL):
        self.model = model

    def run(self, topic: str) -> str:
        prompt = (
            "You are an assistant that prepares a short research brief for a blog.\n\n"
            f"Topic: {topic}\n\n"
            "Write:\n"
            "- A concise 3–4 sentence background summary\n"
            "- Key subtopics to cover\n"
            "- Three quick facts or sources (names or keywords only, no URLs)"
        )

        logging.info("ResearchAgent: calling Gemini for topic expansion")

        # ❗ No max_output_tokens or max_tokens
        response = call_gemini(prompt, model=self.model)

        return response.strip()
