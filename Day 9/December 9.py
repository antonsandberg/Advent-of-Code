import numpy as np

with open('inputDec9.txt', 'r') as f:
    lines = f.read().strip().split()
    modified_lines = []
    for line in lines:
        modified_line = []
        for num in line:
            modified_line.append(int(num))
        modified_lines.append(modified_line)

X = np.array(modified_lines)


max_col_i = np.size(X, 1)-1
max_row_i = np.size(X, 0)-1
print(max_col_i, max_row_i)
risk_levels = []
for y, row in enumerate(X):
    for x, col in enumerate(row):
        neighborhood = ((1, 0), (0, 1), (-1, 0), (0, -1)) # down, right, up, left
        neighborhood_topleft = ((1, 0), (0, 1)) # down, right
        neighborhood_topright = ((1, 0), (0, -1)) # down, left
        neighborhood_top = ((1, 0), (0, 1), (0, -1)) # down, right, left
        neighborhood_downleft = ((0, 1), (-1, 0)) # right, up
        neighborhood_down = ((0, 1), (0, -1), (-1, 0)) # right, left, up
        neighborhood_downright = ((0, -1), (-1, 0)) # left, up
        neighborhood_right = ((1, 0), (-1, 0), (0, -1)) # down, up, left
        neighborhood_left = ((1, 0), (-1, 0), (0, 1)) # down, up, right

        if y == 0:
            if x == 0:
                neighbor_numbers = []
                for dy, dx in neighborhood_topleft:
                    neighbor_numbers.append(X[y+dy, x+dx])
                if col < min(neighbor_numbers):
                    risk_levels.append(col + 1)

            elif x == max_col_i:
                neighbor_numbers = []
                for dy, dx in neighborhood_topright:
                    neighbor_numbers.append(X[y+dy, x+dx])
                if col < min(neighbor_numbers):
                    risk_levels.append(col + 1)     
            else:
                neighbor_numbers = []
                for dy, dx in neighborhood_top:
                    neighbor_numbers.append(X[y+dy, x+dx])
                if col < min(neighbor_numbers):
                    risk_levels.append(col + 1)  
        elif y == max_row_i:
            if x == 0:
                neighbor_numbers = []
                for dy, dx in neighborhood_downleft:
                    neighbor_numbers.append(X[y+dy, x+dx])
                if col < min(neighbor_numbers):
                    risk_levels.append(col + 1)

            elif x == max_col_i:
                neighbor_numbers = []
                for dy, dx in neighborhood_downright:
                    neighbor_numbers.append(X[y+dy, x+dx])
                if col < min(neighbor_numbers):
                    risk_levels.append(col + 1)     
            else:
                neighbor_numbers = []
                for dy, dx in neighborhood_down:
                    neighbor_numbers.append(X[y+dy, x+dx])
                if col < min(neighbor_numbers):
                    risk_levels.append(col + 1)

        elif x == 0:
                neighbor_numbers = []
                for dy, dx in neighborhood_left:
                    neighbor_numbers.append(X[y+dy, x+dx])
                if col < min(neighbor_numbers):
                    risk_levels.append(col + 1)
        
        elif x == max_col_i:
                neighbor_numbers = []
                for dy, dx in neighborhood_right:
                    neighbor_numbers.append(X[y+dy, x+dx])
                if col < min(neighbor_numbers):
                    risk_levels.append(col + 1)
        
        else:
                neighbor_numbers = []
                for dy, dx in neighborhood:
                    neighbor_numbers.append(X[y+dy, x+dx])
                if col < min(neighbor_numbers):
                    risk_levels.append(col + 1)

print(sum(risk_levels))


# B

        

 



