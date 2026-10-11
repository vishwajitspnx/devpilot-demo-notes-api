import pytest
from fastapi.testclient import TestClient

import app.main as main
from app.store import NoteStore


@pytest.fixture
def client(monkeypatch):
    monkeypatch.setattr(main, "store", NoteStore())
    return TestClient(main.app)


def test_export_markdown(client):
    client.post("/api/notes", json={"title": "Groceries", "body": "milk"})
    r = client.get("/api/export.md")
    assert r.status_code == 200
    assert r.headers["content-type"].startswith("text/markdown")
    assert "## Groceries" in r.text
    assert "milk" in r.text
