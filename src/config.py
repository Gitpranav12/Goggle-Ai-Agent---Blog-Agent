from dataclasses import dataclass
import os

from dotenv import load_dotenv

load_dotenv()


@dataclass
class Settings:
    groq_api_key: str
    tavily_api_key: str
    default_model: str


def get_settings() -> Settings:
    groq_key = os.getenv("GROQ_API_KEY")
    tavily_key = os.getenv("TAVILY_API_KEY")
    model = os.getenv("DEFAULT_MODEL", "llama-3.3-70b-versatile")

    if not groq_key:
        raise RuntimeError("GROQ_API_KEY missing in .env")

    if not tavily_key:
        raise RuntimeError("TAVILY_API_KEY missing in .env")

    return Settings(
        groq_api_key=groq_key,
        tavily_api_key=tavily_key,
        default_model=model,
    )
