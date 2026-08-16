CREATE TABLE IF NOT EXISTS subscribers (
  id TEXT PRIMARY KEY,
  email TEXT NOT NULL UNIQUE,
  status TEXT NOT NULL CHECK(status IN ('pending','active','suppressed')),
  cadence TEXT NOT NULL CHECK(cadence IN ('as_verified','daily','weekly','monthly','annually')),
  include_json TEXT NOT NULL DEFAULT '{}',
  exclude_json TEXT NOT NULL DEFAULT '{}',
  confirm_token_hash TEXT,
  manage_token_hash TEXT,
  created_at TEXT NOT NULL,
  confirmed_at TEXT,
  updated_at TEXT NOT NULL,
  last_sent_at TEXT
);

CREATE INDEX IF NOT EXISTS idx_subscribers_status_cadence ON subscribers(status, cadence);

CREATE TABLE IF NOT EXISTS published_items (
  id TEXT PRIMARY KEY,
  title TEXT NOT NULL,
  canonical_url TEXT NOT NULL,
  summary TEXT NOT NULL,
  models_json TEXT NOT NULL DEFAULT '[]',
  brands_json TEXT NOT NULL DEFAULT '[]',
  topics_json TEXT NOT NULL DEFAULT '[]',
  published_at TEXT NOT NULL,
  created_at TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_published_items_published_at ON published_items(published_at);

CREATE TABLE IF NOT EXISTS deliveries (
  subscriber_id TEXT NOT NULL,
  publication_id TEXT NOT NULL,
  delivered_at TEXT NOT NULL,
  PRIMARY KEY (subscriber_id, publication_id)
);
