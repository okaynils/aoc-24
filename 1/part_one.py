INPUT = "input.txt"

left = []
right = []

with open(INPUT, "r") as f:
    for line in f:
        split = line.split("   ")
        left.append(int(split[0]))
        right.append(int(split[1]))

sum = 0

left.sort()
right.sort()

for i in range(len(left)):
    sum += abs(left[i] - right[i])

print(f'Solution: {sum}')