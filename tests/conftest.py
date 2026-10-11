import pytest
from fastapi.testclient import TestClient

import app.main as main
from app.store import NoteStore


@pytest.fixture
def client(monkeypatch):
    monkeypatch.setattr(main, "store", NoteStore())  # a fresh, empty store for every test
    return TestClient(main.app)
