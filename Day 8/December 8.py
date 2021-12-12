from itertools import permutations

with open('TestInputDec8.txt', 'r') as f:
    lines = f.readlines()
    modified_lines = []
    modified_lines_b = []
    for line in lines:
        modified_lines_b.append(line.strip())
        modified_line = line.split('|', 1)[1]
        modified_lines.append(modified_line.strip().split())

count = 0
for line in modified_lines:
    for expression in line:
        x = len(expression)
        if (x == 2) or (x == 3) or (x == 4) or (x == 7):
            count += 1

print(count)

# B



for line in modified_lines_b:
    left_side, right_side = line.split('|')
    left_side = left_side.split()
    right_side = right_side.split()

["".join(p) for p in permutations('acedgfb')]
