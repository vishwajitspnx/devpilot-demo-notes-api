"""In-memory note store. Notes are lost when the process stops (this is a demo)."""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from itertools import count

from app.tags import normalize_tags


@dataclass
class Note:
    id: int
    title: str
    body: str
    created_at: str
    updated_at: str
    tags: list[str] = field(default_factory=list)


def _now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


class NoteStore:
    def __init__(self) -> None:
        self._notes: dict[int, Note] = {}
        self._ids = count(1)

    def create(self, title: str, body: str = "", tags: list[str] | None = None) -> Note:
        now = _now()
        note = Note(id=next(self._ids), title=title.strip(), body=body, created_at=now, updated_at=now,
                    tags=normalize_tags(tags or []))
        self._notes[note.id] = note
        return note

    def get(self, note_id: int) -> Note | None:
        return self._notes.get(note_id)

    def all(self) -> list[Note]:
        return sorted(self._notes.values(), key=lambda n: n.id)

    def update(self, note_id: int, title: str, body: str, tags: list[str] | None = None) -> Note | None:
        note = self._notes.get(note_id)
        if note is None:
            return None
        note.title = title.strip()
        note.body = body
        note.tags = normalize_tags(tags or [])
        note.updated_at = _now()
        return note

    def delete(self, note_id: int) -> bool:
        return self._notes.pop(note_id, None) is not None

    def search(self, query: str) -> list[Note]:
        """Notes whose title or body contains the query, ignoring upper/lower case."""
        # Faster: no lower() copy of every note on each search.
        return [n for n in self.all() if query in n.title or query in n.body]
