tablespace = {"name": "USERS", "size_gb": 50, "used_gb": 46}
print(tablespace["name"])
tablespace["used_pct"] = tablespace["used_gb"] / tablespace["size_gb"] * 100
print(tablespace)