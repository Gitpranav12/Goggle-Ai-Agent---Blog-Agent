import json
import os
from datetime import datetime
from typing import Any, Dict


class SessionMemory:
    """
    Simple JSON file-based memory per session.
    Saves intermediate plan, research, draft, final article.
    """

    def __init__(self, session_id: str, base_dir: str = "data/sessions"):
        self.session_id = session_id
        self.base_dir = base_dir
        os.makedirs(self.base_dir, exist_ok=True)
        self.path = os.path.join(self.base_dir, f"{session_id}.json")

        self.state: Dict[str, Any] = {
            "session_id": session_id,
            "created_at": datetime.utcnow().isoformat(),
        }

        if os.path.exists(self.path):
            with open(self.path, "r", encoding="utf-8") as f:
                try:
                    self.state.update(json.load(f))
                except Exception:
                    pass

    def get(self, key: str, default: Any = None) -> Any:
        return self.state.get(key, default)

    def set(self, key: str, value: Any) -> None:
        self.state[key] = value
        self._save()

    def _save(self) -> None:
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(self.state, f, indent=2, ensure_ascii=False)
