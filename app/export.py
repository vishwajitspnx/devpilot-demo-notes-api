"""Export all notes as one Markdown document."""

from app.store import Note


def to_markdown(notes: list[Note]) -> str:
    lines = ["# My notes", ""]
    for note in notes:
        lines.append(f"## {note.title}")
        lines.append("")
        lines.append(f"_Last changed {note.updated_at}_")
        lines.append("")
        if note.body:
            lines.append(note.body)
            lines.append("")
    return "\n".join(lines)
