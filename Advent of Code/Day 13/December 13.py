import numpy as np

with open('inputDec13.txt', 'r') as f:
    lines = f.read().strip().split()

folds = [[0, 655], [447, 0], [0, 327], [223, 0],
        [0, 163], [111, 0], [0, 81], [55, 0],
        [0, 40], [27, 0], [13, 0], [6, 0]]
fold_test = [[7, 0], [0, 5]]



coords = []

for line in lines:
    if len(line.split(',')) == 2:
        coord = line.split(',')
        coords.append([int(coord[0]), int(coord[1])])


coords_check = np.array(coords)
max_y = max(coords_check[:, 1])
max_x = max(coords_check[:, 0])

matrix = np.zeros((max_y+1, max_x+1))

for coord in coords:
    matrix[coord[1],coord[0]] = 1


for fold in folds:
    if fold[0] > 0:
        up = matrix[0:fold[0], :]
        down = matrix[fold[0]+1:, :]
        reverse_down = np.flipud(down)
        new_matrix = up + reverse_down
        new_matrix[1 < new_matrix] = 1
    else:
        left = matrix[:, 0:fold[1]]
        right = matrix[:, fold[1]+1:]
        reverse_right = np.fliplr(right)
        new_matrix = left + reverse_right
        new_matrix[1 < new_matrix] = 1
    matrix = new_matrix
    print(np.sum(matrix))

str_matrix = []
for row in matrix:
    str_row = ["." if (x == 0) else "#" for x in row]
    str_row = "".join(str_row)
    str_matrix.append(str_row)

for row in str_matrix:
    print(row)
