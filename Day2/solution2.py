def is_report_safe(report):

    for i in range(len(report) - 1):
        diff = abs(report[i] - report[i + 1])
        if diff < 1 or diff > 3:
            return False

    increasing = all(report[i] < report[i + 1] for i in range(len(report) - 1))
    decreasing = all(report[i] > report[i + 1] for i in range(len(report) - 1))

    return increasing or decreasing

def count_safe_report(file_path):

    count = 0

    with open(file_path, 'r') as f:
        for line in f:

            report = list(map(int, line.split()))

            if is_report_safe(report):
                count += 1

    return count

file_path = "input.txt"

safe_reports = count_safe_report(file_path)

print(safe_reports)