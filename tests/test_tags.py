from app.tags import normalize_tags


def test_normalize_tags():
    assert normalize_tags([" Work ", "work", "Big Ideas", ""]) == ["work", "big-ideas"]


def test_tags_are_saved_on_a_note(client):
    r = client.post("/api/notes", json={"title": "Plan", "tags": ["Work", "work"]})
    assert r.json()["tags"] == ["work"]


def test_filter_by_tag(client):
    client.post("/api/notes", json={"title": "Plan", "tags": ["work"]})
    client.post("/api/notes", json={"title": "Cake", "tags": ["home"]})
    assert [n["title"] for n in client.get("/api/notes", params={"tag": "Work"}).json()] == ["Plan"]
