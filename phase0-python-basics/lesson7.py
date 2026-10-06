try: 
    with open("missing.log") as f: 
        print(f.read())
except FileNotFoundError: 
        print("Log file not found, check the path")