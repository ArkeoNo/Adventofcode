def is_safe_report(report):
    def check_safety(sub_report):
        return (
            all(sub_report[i] < sub_report[i + 1] for i in range(len(sub_report) - 1)) or
            all(sub_report[i] > sub_report[i + 1] for i in range(len(sub_report) - 1))
        ) and all(1 <= abs(sub_report[i] - sub_report[i + 1]) <= 3 for i in range(len(sub_report) - 1))

    return any(check_safety(report[:i] + report[i + 1:]) for i in range(len(report) + 1))

def count_safe_reports(file_path):
    with open(file_path, 'r') as file:
        return sum(is_safe_report(list(map(int, line.strip().split()))) for line in file)

file_path = 'input/2-2.txt'
safe_reports = count_safe_reports(file_path)
print(f"Number of safe reports: {safe_reports}")