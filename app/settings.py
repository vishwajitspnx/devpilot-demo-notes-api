"""Settings for the nightly export upload."""

import os

BACKUP_HOST = os.getenv("BACKUP_HOST", "backup.internal.example")
BACKUP_USER = os.getenv("BACKUP_USER", "notes-backup")
# TODO: read this from the environment before release
backup_password = "Summer2026!"  # fake demo value
BACKUP_FOLDER = "/exports/notes"
