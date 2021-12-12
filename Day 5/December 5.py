import numpy as np

# A
with open('inputDec5.txt', 'r') as f:
    data = f.read().split('\n')
    data.pop(-1)
    coordinates = []
    for line in data:
        coordinate = line.split('->')
        pairs = []
        for i in coordinate:
            indexs = []
            j = i.split(',')
            for k in j:
                indexs.append(int(k))
            pairs.append(indexs)
        coordinates.append(pairs)



branchCrossings = np.zeros((1000,1000))

for line in coordinates:
    if (line[0][0] == line[1][0]):
        x = line[0][0]
        (y1, y2) = sorted([line[0][1], line[1][1]])
        for i in range(y1, y2+1):
            branchCrossings[x][i] += 1
    elif (line[0][1] == line[1][1]):
        y = line[0][1]
        (x1, x2) = sorted([line[0][0], line[1][0]])
        for i in range(x1, x2+1):
            branchCrossings[i][y] += 1


intersections = branchCrossings > 1
print(np.count_nonzero(intersections))

# B

branchCrossings = np.zeros((990,990))
for line in coordinates:
    print(line)
    if (line[0][0] == line[1][0]):
        x = line[0][0]
        (y1, y2) = sorted([line[0][1], line[1][1]])
        for i in range(y1, y2+1):
            branchCrossings[x][i] += 1
    elif (line[0][1] == line[1][1]):
        y = line[0][1]
        (x1, x2) = sorted([line[0][0], line[1][0]])
        for i in range(x1, x2+1):
            branchCrossings[i][y] += 1
    else:
        x1, x2 = [line[0][0], line[1][0]]
        y1, y2 = [line[0][1], line[1][1]]
        if x1 < x2:
            if y1 < y2:
                for i, j in zip(range(x1, x2+1), range(y1, y2+1)):
                    branchCrossings[i][j] += 1
            elif y1 > y2:
                for i, j in zip(range(x1, x2+1), reversed(range(y2, y1+1))):
                    branchCrossings[i][j] += 1
        elif x1 > x2:
            if y1 < y2:
                    for i, j in zip(reversed(range(x2, x1+1)), range(y1, y2+1)):
                        branchCrossings[i][j] += 1
            elif y1 > y2:
                    for i, j in zip(reversed(range(x2, x1+1)), reversed(range(y2, y1+1))):
                        branchCrossings[i][j] += 1



intersections = branchCrossings > 1
print(np.count_nonzero(intersections))
