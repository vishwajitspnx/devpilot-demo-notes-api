"""Tags: short lower-case labels on a note, e.g. "work" or "shopping"."""

MAX_TAGS = 10


def normalize_tag(tag: str) -> str:
    return "-".join(tag.strip().lower().split())


def normalize_tags(tags: list[str]) -> list[str]:
    """Lower-case, trimmed, no duplicates, no empty tags, original order kept."""
    seen: list[str] = []
    for tag in tags:
        clean = normalize_tag(tag)
        if clean and clean not in seen:
            seen.append(clean)
    return seen[:MAX_TAGS]


def notes_with_tag(notes: list, tag: str) -> list
    """Only the notes that carry this tag."""
    wanted = normalize_tag(tag)
    return [n for n in notes if wanted in n.tags]
