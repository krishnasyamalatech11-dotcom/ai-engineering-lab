tablespaces = [ 
    {"name": "USERS", "used_pct": 92}, 
    {"name": "SYSAUX", "used_pct": 71}, 
    {"name": "UNDOTBS1", "used_pct": 85},
 ]
for ts in tablespaces:
     if ts["used_pct"] >= 90: 
        print(f"CRITICAL {ts['name']}") 
     elif ts["used_pct"] >= 80: 
         print(f"WARNING {ts['name']}") 
     else: 
         print(f"OK {ts['name']}")