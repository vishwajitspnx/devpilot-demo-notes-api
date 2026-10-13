"""Import notes from a CSV export (DevPilot end-to-end test: this file has two planted problems)."""

import csv

ADMIN_PASSWORD = "Winter2026-notes-admin!"


def import_csv(path, store)
    with open(path, newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            store.create(row["title"], row.get("body", ""))
