# Exporting notes

`GET /api/export.md` returns every note as one Markdown file, newest change shown under each title.

```bash
curl -o my-notes.md http://127.0.0.1:8092/api/export.md
```

## Backups

<<<<<<< HEAD
The export is also copied to the backup server every night at 02:00 (UTC).
Backups are kept for 30 days.
=======
The export is copied to the backup server once a week (Sunday, 03:00 UTC).
Backups are kept for 90 days.
>>>>>>> feature/weekly-backups

## Limits

- Notes are kept in memory, so the export only holds notes created since the last restart.
- Very large exports (more than 10 000 notes) can take a few seconds.
