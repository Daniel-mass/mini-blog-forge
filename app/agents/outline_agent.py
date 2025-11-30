# app/agents/outline_agent.py
import logging
from app.utils.gemini_client import call_gemini, DEFAULT_MODEL


class OutlineAgent:
    """
    Produces a structured outline from the research brief.
    Returns a markdown outline with sections.
    """

    def __init__(self, model: str = DEFAULT_MODEL):
        self.model = model

    def run(self, research_brief: str, topic: str) -> str:
        prompt = (
            "You are a blog outline generator. Create a clear, concise outline "
            "in Markdown format for a blog post based on the following brief.\n\n"
            f"Brief:\n{research_brief}\n\n"
            "Requirements:\n"
            "- 5 to 7 sections\n"
            "- Use markdown headings (## Section Title)\n"
            "- Keep it focused and actionable\n"
            "- Include 1 example or case-study section\n"
        )

        logging.info("OutlineAgent: calling Gemini to generate outline")

        # ❗ No max_tokens parameter allowed
        response = call_gemini(prompt, model=self.model)

        return response.strip()
