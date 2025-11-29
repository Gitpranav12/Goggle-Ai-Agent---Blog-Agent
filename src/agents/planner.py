from typing import Dict, Any
import json


class PlannerAgent:
    """
    Plans article structure: sections + SEO + read time.
    """

    def __init__(self, client, model: str):
        self.client = client
        self.model = model

    def plan(
        self,
        topic: str,
        audience: str,
        tone: str,
        language: str,
        target_length: str,
    ) -> Dict[str, Any]:
        system_prompt = (
            "You are a blog content strategist. "
            "Create a structured blog outline as JSON with keys:\n"
            "- sections: list of {title, description}\n"
            "- seo_keywords: list of strings\n"
            "- estimated_read_time_minutes: integer\n"
            "Return ONLY valid JSON, no prose."
        )

        user_prompt = (
            f"Topic: {topic}\n"
            f"Audience: {audience}\n"
            f"Tone: {tone}\n"
            f"Language: {language}\n"
            f"Target length: {target_length}\n"
        )

        resp = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0.6,
        )

        content = resp.choices[0].message.content

        try:
            plan = json.loads(content)
        except Exception:
            # fallback: everything in single section
            plan = {
                "sections": [
                    {
                        "title": "Main Article",
                        "description": topic,
                    }
                ],
                "seo_keywords": [],
                "estimated_read_time_minutes": 5,
            }

        if not isinstance(plan.get("sections", []), list):
            plan["sections"] = [plan["sections"]]

        return plan
