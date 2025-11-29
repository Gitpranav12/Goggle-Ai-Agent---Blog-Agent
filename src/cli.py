from rich.console import Console
from rich.prompt import Prompt

from .orchestrator import OmniBlogOrchestrator

console = Console()


def main():
    console.print("[bold magenta]OmniBlog Agent Studio (Groq Edition)[/bold magenta]\n")

    topic = Prompt.ask("Enter blog topic")
    audience = Prompt.ask(
        "Target audience (e.g. Beginner software developers)",
        default="Beginner software developers",
    )
    tone = Prompt.ask(
        "Desired tone (e.g. Friendly and practical)",
        default="Friendly and practical",
    )
    language = Prompt.ask(
        "Blog language (e.g. English, Hindi, Spanish)",
        default="English",
    )
    target_length = Prompt.ask(
        "Target length (e.g. 800 words, short, long)",
        default="800 words",
    )

    orchestrator = OmniBlogOrchestrator()
    orchestrator.run(
        topic=topic,
        audience=audience,
        tone=tone,
        language=language,
        target_length=target_length,
    )


if __name__ == "__main__":
    main()
