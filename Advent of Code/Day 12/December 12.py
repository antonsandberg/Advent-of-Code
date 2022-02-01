from collections import defaultdict, deque
from pprint import pprint


def is_small(cave):
    return cave.islower()


with open('inputDec12.txt') as f:
    data =[x.split('-') for x in f.read().strip().split()]
    
adj = defaultdict(list)

for a, b in data:
    adj[a].append(b)
    adj[b].append(a)

# Number of paths
global ans
ans = 0

# Deapth First Search
visited = set()

def dfs(cave):
    global ans

    if cave == "end":
        ans += 1
        return

    if is_small(cave) and cave in visited:
        return

    if is_small(cave):
        visited.add(cave)

    for nbr in adj[cave]:
        if nbr == "start":
            continue
        dfs(nbr)

    # At the end, remove from the dfs
    if is_small(cave):
        visited.remove(cave)

dfs("start")

print(ans)