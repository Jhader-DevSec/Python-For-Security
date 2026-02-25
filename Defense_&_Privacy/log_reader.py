def log_analyzer(file_path):
    with open(file_path, "r") as log_file:
        for line in log_file:
            if "Failed password" in line:
                yield line
                
for l in log_analyzer("log_reader.txt"):
    print(l)
    print("-" * 50)