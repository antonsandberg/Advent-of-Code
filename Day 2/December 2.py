import numpy as np

with open('inputDec2.txt', 'r') as f:
    lines = f.readlines()
    instructions = []
    values = []
    for i, line in enumerate(lines):
        instruction, value = line.split()
        values.append(value)
        instructions.append(instruction)

horisontalPosition = 0
verticalPosition = 0
X = 0
for instruction, value in zip(instructions, values):
    if instruction == 'forward':
        horisontalPosition += int(value)
        verticalPosition += X*int(value)
    elif instruction == 'up':
        X -= int(value)
    else:
        X += int(value)

print(f'horisontal value={horisontalPosition} vertical value={verticalPosition} and product={horisontalPosition*verticalPosition}')
