# MiniBlogForge – AI Blog Generation Agent

MiniBlogForge is a multi-agent AI system designed to automate the creation of high-quality blog posts. Using a modular agent-based architecture, it researches topics, generates structured outlines, drafts blog posts, and saves them in Markdown format. This project showcases the power of agent orchestration for content generation.

---

## Problem Statement

Writing blogs manually is time-consuming and repetitive. Researching, structuring, drafting, and editing can take hours for each article. Maintaining a consistent tone and format across multiple posts is mentally exhausting, and scaling content production without sacrificing quality is challenging.  

MiniBlogForge automates these steps, allowing writers to focus on strategic insights and creative refinement while AI handles research, drafting, and formatting.

---

## Solution Statement

MiniBlogForge uses specialized AI agents to:  
- **Research:** Gather and synthesize key insights about a topic.  
- **Outline:** Generate structured markdown outlines with actionable sections.  
- **Draft:** Produce full blog posts in Markdown format based on research and outline.

This workflow reduces the blank-page problem, accelerates content production, and maintains consistent quality.

---

## Architecture

MiniBlogForge follows a modular, sequential architecture with three primary agents:

1. **ResearchAgent:** Generates a concise research brief for a given topic.  
2. **OutlineAgent:** Produces a structured outline with 5–7 markdown sections, including example or case-study suggestions.  
3. **DraftAgent:** Writes the blog post in Markdown using the research brief and outline.

A central orchestrator, **MiniBlogFlow**, coordinates these agents, manages sessions, and saves outputs to files.  

Additional utilities include:  
- `save_markdown`: Saves the generated blog to a Markdown file.  
- Session management API: Tracks job status and retrieves results.

---

## Workflow

1. **Submit a topic** via API `/generate`.  
2. **ResearchAgent** creates a short research brief.  
3. **OutlineAgent** generates a structured outline.  
4. **DraftAgent** produces a full blog draft in Markdown.  
5. **Result retrieval** via `/result/{session_id}` API endpoint returns the full blog content and file path.

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST   | `/generate` | Start a blog generation session with `topic`, `tone`, and `length`. Returns `session_id`. |
| GET    | `/status/{session_id}` | Check session status (`queued`, `running`, `completed`, `failed`). |
| GET    | `/result/{session_id}` | Retrieve full blog content and file path after completion. |

**Example request:**
```bash
POST /generate
{
  "topic": "AI Agents",
  "tone": "informative",
  "length": "short"
}
