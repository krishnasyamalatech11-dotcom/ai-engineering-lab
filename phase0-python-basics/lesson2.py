databases = ["ORCL", "PGPROD", "MONGO01"]
print(databases[0]) # first item: ORCL
databases.append("PGTEST")
print(len(databases)) # 4
for db in databases: print("Checking", db)