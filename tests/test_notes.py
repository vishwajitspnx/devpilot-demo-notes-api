def test_health(client):
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok", "notes": 0}


def test_create_and_get(client):
    r = client.post("/api/notes", json={"title": "  Groceries ", "body": "milk, eggs"})
    assert r.status_code == 201
    note = r.json()
    assert note["id"] == 1
    assert note["title"] == "Groceries"
    assert client.get("/api/notes/1").json()["body"] == "milk, eggs"


def test_empty_title_is_rejected(client):
    assert client.post("/api/notes", json={"title": ""}).status_code == 422


def test_list_is_sorted_by_id(client):
    for title in ["b", "a", "c"]:
        client.post("/api/notes", json={"title": title})
    assert [n["title"] for n in client.get("/api/notes").json()] == ["b", "a", "c"]


def test_update(client):
    client.post("/api/notes", json={"title": "Old"})
    r = client.put("/api/notes/1", json={"title": "New", "body": "changed"})
    assert r.status_code == 200
    assert r.json()["title"] == "New"


def test_update_missing_note_is_404(client):
    assert client.put("/api/notes/99", json={"title": "x"}).status_code == 404


def test_delete(client):
    client.post("/api/notes", json={"title": "Temp"})
    assert client.delete("/api/notes/1").status_code == 204
    assert client.get("/api/notes/1").status_code == 404


def test_search_is_case_insensitive(client):
    client.post("/api/notes", json={"title": "Shopping List", "body": "Bread"})
    client.post("/api/notes", json={"title": "Ideas", "body": "Learn to juggle"})
    assert [n["title"] for n in client.get("/api/notes", params={"q": "shopping"}).json()] == ["Shopping List"]
    assert [n["title"] for n in client.get("/api/notes", params={"q": "JUGGLE"}).json()] == ["Ideas"]
