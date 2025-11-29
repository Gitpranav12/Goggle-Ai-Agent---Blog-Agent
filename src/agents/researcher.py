from typing import Dict, Any, List

from ..tools.web_search import WebSearchTool
from ..tools.notes_store import NotesStore


class ResearcherAgent:
    """
    Uses Tavily web search + Groq to summarize research per section.
    """

    def __init__(
        self,
        client,
        model: str,
        search_tool: WebSearchTool,
        notes_store: NotesStore,
    ):
        self.client = client
        self.model = model
        self.search_tool = search_tool
        self.notes_store = notes_store

    def research_sections(self, sections: List[Dict[str, Any]]) -> Dict[str, Any]:
        research_summary: Dict[str, Any] = {}

        for section in sections:
            title = section.get("title", "Section")
            description = section.get("description", "")
            query = f"{title} - {description}"

            results = self.search_tool.search(query, max_results=3)

            text_block = "\n\n".join(
                f"{r['title']} ({r['url']}): {r['content']}"
                for r in results
                if r.get("content")
            )

            summary = self._summarize(title, text_block)
            research_summary[title] = {
                "summary": summary,
                "sources": [r["url"] for r in results if r.get("url")],
            }

            self.notes_store.add_note(title, summary)

        return research_summary

    def _summarize(self, section_title: str, text_block: str) -> str:
        if not text_block.strip():
            return "No strong web results; rely on core knowledge."

        system_prompt = (
            "You are a neutral research assistant. "
            "Given some noisy web snippets, write a clean, factual summary "
            "for the given section. Avoid marketing fluff."
        )

        user_prompt = (
            f"Section: {section_title}\n\n"
            f"Snippets:\n{text_block[:6000]}"
        )

        resp = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0.4,
        )

        return resp.choices[0].message.content.strip()
