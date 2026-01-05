def read_log_file(file_path):
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
            print(f"Total log lines read: {len(lines)}")
            return lines
    except FileNotFoundError:
        print("Log file not found.")
        return []


if __name__ == "__main__":
    log_file_path = "logs/sample.log.example"
    log_lines = read_log_file(log_file_path)

    for line in log_lines:
        print(line.strip())
