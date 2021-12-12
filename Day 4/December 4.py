
with open('inputDec4.txt', 'r') as f:
    data = f.read().split('\n\n')
draws = [int(i) for i in data[0].split(',')]
boards = [[[int(i) for i in line.split()] for line in board.split('\n')] for board in data[1:]]


numbers = []
results = []
winningPlayers = []
for number in draws:
    numbers.append(number)
    for i, player in enumerate(boards):
        for row in player:
            count = 0
            for elem in row:
                if elem in numbers:
                    count += 1
                    if count == 5:
                        sum = 0
                        for row2 in player:
                            for elem2 in row2:
                                if elem2 not in numbers:
                                    sum += elem2
                        if i not in winningPlayers:
                            winningPlayers.append(i)
                            results.append(sum*number)


print(results[0], results[-1])
