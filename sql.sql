CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    diamonds REAL DEFAULT 0.0,
    energy INTEGER DEFAULT 500,
    referrals INTEGER DEFAULT 0
);
