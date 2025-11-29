import os
from datetime import datetime
from typing import Dict, Any, Optional

from groq import Groq
from rich.console import Console
from rich.panel import Panel

from .config import get_settings
from .memory.session_memory import SessionMemory
from .tools.web_search import WebSearchTool
from .tools.notes_store import NotesStore
from .agents.planner import PlannerAgent
from .agents.researcher import ResearcherAgent
from .agents.writer import WriterAgent
from .agents.editor import EditorAgent

console = Console()


class OmniBlogOrchestrator:
    """
    Coordinates all agents & memory.
    """

    def __init__(self):
        self.settings = get_settings()
        self.client = Groq(api_key=self.settings.groq_api_key)

        self.search_tool = WebSearchTool(api_key=self.settings.tavily_api_key)
        self.notes_store = NotesStore()

        self.planner = PlannerAgent(self.client, self.settings.default_model)
        self.researcher = ResearcherAgent(
            self.client,
            self.settings.default_model,
            self.search_tool,
            self.notes_store,
        )
        self.writer = WriterAgent(self.client, self.settings.default_model)
        self.editor = EditorAgent(self.client, self.settings.default_model)

    def new_session_id(self) -> str:
        return datetime.utcnow().strftime("session-%Y%m%d-%H%M%S")

    def run(
        self,
        topic: str,
        audience: str,
        tone: str,
        language: str,
        target_length: str,
        session_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        if session_id is None:
            session_id = self.new_session_id()

        memory = SessionMemory(session_id)

        console.print(Panel(f"[bold cyan]Starting session {session_id}[/bold cyan]"))

        # 1) Planning
        console.print("[bold yellow]1) Planning article structure...[/bold yellow]")
        plan = self.planner.plan(topic, audience, tone, language, target_length)
        memory.set("topic", topic)
        memory.set("audience", audience)
        memory.set("tone", tone)
        memory.set("language", language)
        memory.set("target_length", target_length)
        memory.set("plan", plan)

        # 2) Research
        console.print("[bold yellow]2) Researching sections...[/bold yellow]")
        research = self.researcher.research_sections(plan["sections"])
        memory.set("research", research)
        memory.set("notes", self.notes_store.as_dict())

        # 3) Writing
        console.print("[bold yellow]3) Writing draft...[/bold yellow]")
        draft = self.writer.write_article(
            topic, audience, tone, language, target_length, plan, research
        )
        memory.set("draft", draft)

        # 4) Editing
        console.print("[bold yellow]4) Editing & finalizing...[/bold yellow]")
        final_article = self.editor.edit(draft, audience, tone, language)
        memory.set("final_article", final_article)

        # Save markdown
        out_dir = "outputs"
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, f"{session_id}_blog.md")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(final_article)

        console.print(
            Panel(
                f"[bold green]Done![/bold green]\n"
                f"Session: [bold]{session_id}[/bold]\n"
                f"Markdown file saved at: [bold]{out_path}[/bold]"
            )
        )

        return {
            "session_id": session_id,
            "plan": plan,
            "research": research,
            "draft": draft,
            "final_article": final_article,
            "output_path": out_path,
        }
