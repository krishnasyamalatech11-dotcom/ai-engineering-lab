SET search_path = dba;

DROP TABLE IF EXISTS incidents, alert_events, tablespaces, databases CASCADE;

CREATE TABLE databases (
  id       serial PRIMARY KEY,
  name     text NOT NULL,
  engine   text NOT NULL,
  env      text NOT NULL,
  host     text NOT NULL,
  size_gb  numeric(10,1) NOT NULL
);

CREATE TABLE tablespaces (
  id       serial PRIMARY KEY,
  db_id    int REFERENCES databases(id),
  name     text NOT NULL,
  size_gb  numeric(10,1) NOT NULL,
  used_gb  numeric(10,1) NOT NULL
);

CREATE TABLE alert_events (
  id          bigserial PRIMARY KEY,
  db_id       int REFERENCES databases(id),
  event_time  timestamptz NOT NULL,
  error_code  text NOT NULL,
  message     text NOT NULL
);

CREATE TABLE incidents (
  id          serial PRIMARY KEY,
  db_id       int REFERENCES databases(id),
  opened_at   timestamptz NOT NULL DEFAULT now(),
  severity    text NOT NULL,
  summary     text NOT NULL,
  root_cause  text,
  resolution  text
);

INSERT INTO databases (name, engine, env, host, size_gb) VALUES
  ('ORCLPRD',  'oracle',     'prod', 'dbhost01', 820.0),
  ('ORCLTST',  'oracle',     'test', 'dbhost02', 210.5),
  ('PGPAY',    'postgresql', 'prod', 'pghost01', 340.0),
  ('PGREPORT', 'postgresql', 'dev',  'pghost02',  45.2),
  ('MONGOAPP', 'mongodb',    'prod', 'mghost01', 150.0);

INSERT INTO tablespaces (db_id, name, size_gb, used_gb) VALUES
  (1, 'USERS', 200, 186), (1, 'SYSAUX', 40, 29), (1, 'UNDOTBS1', 60, 52),
  (2, 'USERS', 50, 21), (2, 'SYSAUX', 20, 18),
  (3, 'pg_default', 400, 340), (4, 'pg_default', 100, 45);

INSERT INTO alert_events (db_id, event_time, error_code, message)
SELECT 1 + floor(random() * 5)::int,
       now() - random() * interval '30 days',
       (ARRAY['ORA-01653','ORA-00060','ORA-04031','ORA-01555','ORA-00600'])[1 + floor(random() * 5)::int],
       'Sample alert-log event'
FROM generate_series(1, 500);

INSERT INTO incidents (db_id, severity, summary, root_cause, resolution) VALUES
  (1, 'P1', 'USERS tablespace full, app inserts failing', 'No autoextend, batch load grew', 'Added datafile, enabled autoextend'),
  (3, 'P2', 'Payment API slow at month end', 'Missing index on payments(created_at)', 'Created index concurrently'),
  (1, 'P2', 'ORA-04031 errors in shared pool', 'Hard parsing from literal SQL', 'Increased shared_pool_size, asked app team for binds');