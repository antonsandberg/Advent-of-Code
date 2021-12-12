import re

boards, numbers = list(), list()
for tokens in [re.split(' +|,', line.strip()) for line in open("inputDec4.txt").readlines()]:
    if (len(tokens) > 5): numbers = [i for i in tokens]
    elif (len(tokens) == 5): boards[-1].extend([i for i in tokens])
    else: boards.append(list())

numWins = 0
for num in numbers:
    for board in (b for b in boards if len(b) > 0):
        try:
            board[board.index(num)] = ""
            for i in range(0,5):
                if len(''.join(board[i::5])) == 0 or len(''.join(board[i*5:][:5])) == 0:
                    if numWins == 0 or numWins == len(boards) - 1:
                        print ("BINGO!!!! " + str(int(num) * sum([int(i) if i.isnumeric() else 0 for i in board])))
                    numWins += 1
                    board.clear()
                    break
        except:
            pass