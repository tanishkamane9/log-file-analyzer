from collections import Counter 

def read_log_file(file_path):
    try:
        with open(file_path, "r") as file:
            return file.readlines()
    except FileNotFoundError:
        print("Log file not found.")
        return []
    
def analyze_logs(log_lines):
    level_counts = {
        "INFO":0,
        "ERROR": 0,
        "WARNING":0,
    }

    error_messages = []
    error_hour = []

    for line in log_lines:
        parts = line.split()

        if len(parts)<4:
            continue

        time_part = parts[1]
        hour = time_part.split(":")[0]
        level = parts[2]
        message = " ".join(parts[3:])

        if level in level_counts:
            level_counts[level]+= 1

        if level =="ERROR":
            error_messages.append(message)
            error_hour.append(hour)

    most_common_error = None
    peak_error_hour = None

    if error_messages:
        most_common_error = Counter(error_messages).most_common(1)[0]

    if error_hour:
        peak_error_hour = Counter(error_hour).most_common(1)[0]

    return level_counts, most_common_error , peak_error_hour


if __name__ == "__main__":
    log_file_path = "logs/sample.log.example"
    
    lines = read_log_file(log_file_path)
    level_counts , common_error , peak_hour = analyze_logs(lines)

    print("\nLOG LEVEL SUMMRY")
    print("--------------------")
    for level, count in level_counts.items():
        print(f"{level}: {count}")

    if common_error:
        print("\nLOG LEVEL SUMMARY")
        print("-------------------")
        print(f"{common_error[0]} ({common_error[1]} times)")

    if peak_hour:
        print("\nPEAK ERROR HOUR")
        print("-------------------")
        print(f"{peak_hour[0]}:00 - {peak_hour[0]}:59 ({peak_hour[1]}errors)")

