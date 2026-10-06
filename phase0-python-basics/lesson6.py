error_count = 0
with open("alert.log") as f: # 'with' closes the file automatically 
    for line in f: 
        if "ORA-" in line: 
            error_count += 1 
            print(line.strip())
print(f"Total ORA- errors: {error_count}")