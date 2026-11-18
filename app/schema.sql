DROP TABLE IF EXISTS submission_attachments;
DROP TABLE IF EXISTS submission_domains;
DROP TABLE IF EXISTS submission_flags;
DROP TABLE IF EXISTS submissions;

CREATE TABLE submissions (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    received_at     TEXT NOT NULL DEFAULT (datetime('now')),
    forwarder_hash  TEXT NOT NULL,
    subject         TEXT,
    sender_address  TEXT,
    sender_domain   TEXT,
    verdict         TEXT NOT NULL CHECK (verdict IN ('phishing', 'suspicious', 'safe')),
    threat_type     TEXT,
    confidence      INTEGER NOT NULL CHECK (confidence BETWEEN 0 AND 100),
    reply_sent      INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE submission_flags (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    submission_id   INTEGER NOT NULL REFERENCES submissions(id) ON DELETE CASCADE,
    code            TEXT NOT NULL
);

CREATE TABLE submission_domains (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    submission_id   INTEGER NOT NULL REFERENCES submissions(id) ON DELETE CASCADE,
    domain          TEXT NOT NULL
);

CREATE TABLE submission_attachments (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    submission_id   INTEGER NOT NULL REFERENCES submissions(id) ON DELETE CASCADE,
    filename        TEXT NOT NULL
);