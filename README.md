# Demo Notes API (DevPilot test project)

A tiny notes API (Python, FastAPI): create, read, update, delete and search notes. Notes live in memory only.
It exists to **try out DevPilot**. Some branches contain **bugs on purpose**.

> Do not deploy this anywhere real. The bugs and the fake passwords in it are deliberate.

## Run it

Docker is all you need.

```bash
docker compose up -d --build                            # the API on http://127.0.0.1:8092
docker compose --profile test run --rm --build test     # unit tests
```

Several copies can run side by side, one per stage. For example, `develop` as the "dev" stage:

```bash
git switch develop
NOTES_PORT=8192 docker compose -p notes-dev up -d --build    # http://127.0.0.1:8192
```

| Page | What |
|---|---|
| `/health` | `{"status": "ok", ...}` when the API is alive |
| `/api/notes` | List notes (`?q=word` searches title and body) and create notes (`POST`) |
| `/api/notes/{id}` | Read (`GET`), change (`PUT`) and delete (`DELETE`) one note |
| `/docs` | The API described by FastAPI |

## Branches (stages)

| Branch | Stage | Deploy workflow |
|---|---|---|
| `develop` | development | none (local copy) |
| `staging` | staging | `deploy-staging.yml` |
| `main` | production | `deploy-production.yml` |

Other branches: `feature/note-tags` and `feature/note-export` (new features, start from `develop`),
and `wip/sqlite-storage` (a developer's work in progress, no pull request).

The deploy workflows only print what they would do: there is no real server.

## Planted problems (what DevPilot should notice)

| Where | Problem | DevPilot today |
|---|---|---|
| `develop` | Search is no longer case-insensitive, a unit test fails, so CI fails | CI failure finding on the development stage |
| PR `feature/note-tags` → `develop` | Python syntax error (missing colon) in `app/tags.py` | Finding (high) |
| same PR | Page 1 of `/api/notes?page=1` skips the first notes (off-by-one in `app/paging.py`) | **Not found yet**: needs AI review (Phase 1b) |
| `feature/note-export` (no PR) | Leftover merge-conflict markers in `docs/export.md` | Finding (high) |
| same branch | Hard-coded password in `app/settings.py` | Finding (high) |
| `wip/sqlite-storage` (no PR) | Hard-coded password in `app/sqlite_store.py` | Finding (high), if developer branches are watched |

`main` and `staging` are clean.
