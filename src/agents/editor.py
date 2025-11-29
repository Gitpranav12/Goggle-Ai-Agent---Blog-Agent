class EditorAgent:
    """
    Final polish: grammar, structure, intro/outro, add checklist.
    """

    def __init__(self, client, model: str):
        self.client = client
        self.model = model

    def edit(self, draft: str, audience: str, tone: str, language: str) -> str:
        system_prompt = (
            "You are a professional editor for technical blogs. "
            "Improve clarity, flow, and formatting of the draft. "
            "Keep the language the same (do not translate). "
            "Keep markdown structure. "
            "At the end, add a final section 'Checklist' with 5–7 bullet points "
            "summarizing what the reader can do next."
        )

        user_prompt = (
            f"Audience: {audience}\nTone: {tone}\nLanguage: {language}\n\n"
            f"Draft article in Markdown:\n\n{draft}"
        )

        resp = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0.5,
        )

        return resp.choices[0].message.content.strip()
