def read_log_file(file_path):
    try:
        with open(file_path, "r") as file:
            return file.readlines()
    except FileNotFoundError:
        print("Log file not found.")
        return []
    
def count_log_levels(log_lines):
    count = {
        "INFO":0,
        "ERROR": 0,
        "WARNING":0,
    }

    for line in log_lines:
        parts = line.split()


        if "ERROR" in parts:
            count["ERROR"] += 1
        elif "WARNING" in parts:
            count["WARNING"] += 1
        elif "INFO" in parts:
            count["INFO"] += 1
    return count


if __name__ == "__main__":
    log_file_path = "logs/sample.log.example"
    
    lines = read_log_file(log_file_path)
    level_counts = count_log_levels(lines)

    print("\nLOG LEVEL SUMMRY")
    print("--------------------")
    for level, count in level_counts.items():
        print(f"{level}: {count}")

