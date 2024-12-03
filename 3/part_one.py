import re

INPUT = "input.txt"

with open(INPUT, "r") as f:
    instructions = f.read()

matches = re.findall(r'mul\(\d+,\d+\)', instructions)

sum = 0

for mul in matches:
    term1, term2 = (mul[4:-1]).split(",")
    sum += int(term1) * int(term2)

print(f'Solution: {sum}')