INPUT = "input.txt"

reports = []

with open(INPUT, "r") as f:
    for line in f:
        reports.append(list(map(int, line.split(" "))))

def is_save(report):
    check = True
    last_num = report[0]
    decreasing = report[0] > report[1]
    for idx in range(1,len(report)):
        if abs(report[idx] - last_num) in [1, 2, 3] and (report[idx-1] > report[idx]) == decreasing:
            last_num = report[idx]
            continue
        else:
            
            check = False
            break

    return check

def is_save_with_removal(report):
    for i in range(len(report)):
        modified_report = report[:i] + report[i + 1:]
        if is_save(modified_report):
            return True
    return False

safe = 0

for report in reports:
    if is_save(report) or is_save_with_removal(report):
        safe += 1
        
print(f'Safe documents: {safe}')