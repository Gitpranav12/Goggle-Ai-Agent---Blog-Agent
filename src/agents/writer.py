from typing import Dict, Any


class WriterAgent:
    """
    Writes full markdown blog from plan + research.
    """

    def __init__(self, client, model: str):
        self.client = client
        self.model = model

    def write_article(
        self,
        topic: str,
        audience: str,
        tone: str,
        language: str,
        target_length: str,
        plan: Dict[str, Any],
        research: Dict[str, Any],
    ) -> str:
        system_prompt = (
            "You are an expert blog writer. "
            "Write a complete blog article in Markdown. "
            "Use clear headings (##) for each section from the plan. "
            "Use bullet points where helpful. "
            "Write in the specified language only."
        )

        user_prompt = (
            f"Topic: {topic}\n"
            f"Audience: {audience}\n"
            f"Tone: {tone}\n"
            f"Language: {language}\n"
            f"Target length: {target_length}\n\n"
            f"PLAN:\n{plan}\n\n"
            f"RESEARCH (per section):\n{research}"
        )

        resp = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0.7,
        )

        return resp.choices[0].message.content
