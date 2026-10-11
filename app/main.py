"""Demo Notes API: create, read, update, delete and search notes (kept in memory)."""

from dataclasses import asdict

from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel, Field

from app.paging import paginate
from app.store import NoteStore

app = FastAPI(title="Demo Notes API", version="1.0.0")
store = NoteStore()


class NoteIn(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    body: str = Field(default="", max_length=10_000)
    tags: list[str] = Field(default_factory=list)


def _found(note_id: int):
    note = store.get(note_id)
    if note is None:
        raise HTTPException(status_code=404, detail=f"Note {note_id} not found")
    return note


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "notes": len(store.all())}


@app.get("/api/notes")
def list_notes(q: str | None = None, page: int | None = None, size: int = 20) -> list[dict] | dict:
    notes = [asdict(n) for n in (store.search(q) if q else store.all())]
    if page is None:
        return notes
    return paginate(notes, page, size)


@app.post("/api/notes", status_code=201)
def create_note(data: NoteIn) -> dict:
    return asdict(store.create(data.title, data.body, data.tags))


@app.get("/api/notes/{note_id}")
def get_note(note_id: int) -> dict:
    return asdict(_found(note_id))


@app.put("/api/notes/{note_id}")
def update_note(note_id: int, data: NoteIn) -> dict:
    _found(note_id)
    return asdict(store.update(note_id, data.title, data.body, data.tags))


@app.delete("/api/notes/{note_id}", status_code=204)
def delete_note(note_id: int) -> Response:
    _found(note_id)
    store.delete(note_id)
    return Response(status_code=204)
