"""Import notes from a CSV export (DevPilot end-to-end test: the planted problems are fixed here)."""

import csv
import os

ADMIN_PASSWORD = os.environ.get("NOTES_ADMIN_PASSWORD", "")


def import_csv(path, store):
    with open(path, newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            store.create(row["title"], row.get("body", ""))
