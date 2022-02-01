import numpy as np

# Part 1
with open('inputDec1.txt', 'r') as f:
    lines = f.readlines()
    numbers = np.zeros(len(lines))
    for i, line in enumerate(lines):
        numbers[i] = int(line.strip("'\'"))

counter = 0
for i in range(len(numbers)-1):
    if numbers[i] < numbers[i+1]:
        counter += 1

# Part 2

counter = 0
for i in range(len(numbers)-3):
    firstNumberA = numbers[i]
    secondNumberA = numbers[i+1]
    thirdNumberA = numbers[i+2]
    firstNumberB = numbers[i+1]
    secondNumberB = numbers[i+2]
    thirdNumberB = numbers[i+3]
    if (firstNumberA+secondNumberA+thirdNumberA) < (firstNumberB+secondNumberB+thirdNumberB):
        counter += 1

print(counter)



