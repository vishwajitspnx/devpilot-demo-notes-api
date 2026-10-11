"""WIP: keep notes in a database instead of memory. Not used by the API yet."""

import sqlite3

DB_PATH = "notes.db"
DB_USER = "notes_app"
DB_PASSWORD = "Autumn2026!"  # fake demo value, for the shared test database


def connect(path: str = DB_PATH) -> sqlite3.Connection:
    conn = sqlite3.connect(path)
    conn.execute(
        "CREATE TABLE IF NOT EXISTS notes ("
        " id INTEGER PRIMARY KEY, title TEXT NOT NULL, body TEXT NOT NULL DEFAULT '',"
        " created_at TEXT NOT NULL, updated_at TEXT NOT NULL)"
    )
    return conn


# TODO: create / get / update / delete / search, same as NoteStore
