INPUT = "input.txt"

left = []
right = []

with open(INPUT, "r") as f:
    for line in f:
        split = line.split("   ")
        left.append(int(split[0]))
        right.append(int(split[1]))
        
score = 0
for num_l in left:
    num_l_count = 0
    for num_r in right:
        if num_l == num_r:
            num_l_count += 1
    score += num_l_count * num_l
    
print(f'Score: {score}')