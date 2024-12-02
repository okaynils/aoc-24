INPUT = "input.txt"

reports = []

with open(INPUT, "r") as f:
    for line in f:
        reports.append(list(map(int, line.split(" "))))
        
safe = 0

for report in reports:
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

    safe += 1 if check else 0
    
print(f'Safe documents: {safe}')