"""Split long lists into pages. Pages are numbered from 1."""

DEFAULT_SIZE = 20
MAX_SIZE = 100


def paginate(items: list, page: int = 1, size: int = DEFAULT_SIZE) -> dict:
    size = max(1, min(size, MAX_SIZE))
    page = max(1, page)
    start = page * size
    return {
        "page": page,
        "size": size,
        "total": len(items),
        "items": items[start:start + size],
    }
