import re

INPUT = "input.txt"

with open(INPUT, "r") as f:
    instructions = f.read()

matches = re.findall(r'mul\(\d+,\d+\)|do\(\)|don\'t\(\)', instructions)

sum = 0

enable_calc = True
for match in matches:
    op = False
    
    if re.match(r'mul\(\d+,\d+\)', match):
        op = True
    if re.match(r'do\(\)', match):
        enable_calc = True
    if re.match(r'don\'t\(\)', match):
        enable_calc = False
    
    if enable_calc and op:
        term1, term2 = (match[4:-1]).split(",")
        sum += int(term1) * int(term2)
        
print(f'Solution: {sum}')