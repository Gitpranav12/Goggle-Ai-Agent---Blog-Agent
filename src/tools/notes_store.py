from typing import Dict, List


class NotesStore:
    """
    In-memory notes for each section (used by researcher).
    """

    def __init__(self):
        self._notes: Dict[str, List[str]] = {}

    def add_note(self, section: str, note: str) -> None:
        self._notes.setdefault(section, []).append(note)

    def get_section_notes(self, section: str) -> List[str]:
        return self._notes.get(section, [])

    def as_dict(self) -> Dict[str, List[str]]:
        return self._notes
