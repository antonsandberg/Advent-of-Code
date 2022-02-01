import numpy as np

def find_neighbors(pos, matrix):
    max_y = np.size(matrix, 0)-1
    max_x = np.size(matrix, 1)-1
    if pos[0] == 0:
        if pos[1] == 0:
            neighbors = ((1, 0), (0, 1), (1, 1))
        elif pos[1] == max_x:
            neighbors = ((1, 0), (0, -1), (1, -1))
        else: 
            neighbors = ((1, 0), (0, 1), (0, -1), (1, -1), (1, 1))
    elif pos[0] == max_y:
        if pos[1] == 0:
            neighbors = ((-1, 0), (0, 1), (-1, 1))
        elif pos[1] == max_x:
            neighbors = ((-1, 0), (0, -1), (-1, -1))
        else:
            neighbors = ((-1, 0), (0, -1), (0, 1), (-1, 1), (-1, -1))
    elif pos[1] == 0:
        neighbors = ((1, 0), (-1, 0), (1, 1), (-1, 1), (0, 1))
    elif pos[1] == max_x:
        neighbors = ((1, 0), (-1, 0), (-1, -1), (1, -1), (0, -1))
    else:
        neighbors = ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1))
    return neighbors


def play(matrix, rounds):
    flashes = 0
    rounds_played = 0

    while rounds_played < rounds:
        matrix += 1
        round_flashes = 0
        while len(np.where(matrix > 9)[0]) > 0:
            for y, numbers in enumerate(matrix):
                for x, num in enumerate(numbers):               
                    if num > 9:
                        neighborhood = find_neighbors([y, x], matrix)
                        for dy, dx in neighborhood:
                            if matrix[y+dy, x+dx] != 0:
                                matrix[y+dy, x+dx] += 1
                        matrix[y, x] = 0
                        flashes += 1
                        round_flashes += 1
        
        rounds_played += 1
        if round_flashes == 100:
            print(f'All octupuses flashes at round: {rounds_played}') 

    return flashes
                
if __name__ == "__main__":
    with open('inputDec11.txt', 'r') as f:
        lines = f.read().strip().split()

    formatted_lines = []
    for line in lines:
        formatted_line = [int(x) for x in line]
        formatted_lines.append(formatted_line)

    matrix = np.array(formatted_lines)

    print(play(matrix, 276))





        