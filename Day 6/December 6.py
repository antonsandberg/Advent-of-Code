
# A
with open('inputDec6.txt', 'r') as f:
    lines = f.read().split(',')
    lines[-1] = lines[-1].strip('\n')
    numLines = []
    for num in lines:
        numLines.append(int(num))

for k in range(256):
    for i, age in enumerate(numLines):
        numLines[i] -= 1
        if age == 0:
            numLines[i] = 6
            numLines.append(9)

print(len(numLines))