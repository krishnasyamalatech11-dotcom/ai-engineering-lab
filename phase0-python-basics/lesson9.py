import json, csv
report = {"db": "ORCL", "errors": {"ORA-01653": 3}}
with open("report.json", "w") as f: 
    json.dump(report, f, indent=2)
with open("report.json") as f: 
    data = json.load(f)
print(data["errors"])
with open("tablespaces.csv", "w", newline="") as f: 
    writer = csv.writer(f) 
    writer.writerow(["name", "used_pct"]) 
    writer.writerow(["USERS", 92])