# lesson10.py
import os
import psycopg
from dotenv import load_dotenv

load_dotenv("../.env") # reads DATABASE_URL

with psycopg.connect(os.environ["DATABASE_URL"]) as conn: 
    rows = conn.execute(""" 
        SELECT d.name, t.name, round(t.used_gb / t.size_gb * 100, 1) AS 
used_pct 
        FROM dba.tablespaces t 
        JOIN dba.databases d ON d.id = t.db_id 
        ORDER BY used_pct DESC 
        """).fetchall()
    
for db, ts, pct in rows: 
    print(f"{db:10} {ts:12} {pct:>6}%")