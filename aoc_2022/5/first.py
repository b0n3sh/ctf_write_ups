#!venv/bin/python3

stack = [
    ['S', 'Z', 'P', 'D', 'L', 'B', 'F', 'C'],
    ['N', 'V', 'G', 'P', 'H', 'W', 'B'],    
    ['F', 'W', 'B', 'J', 'G'],
    ['G', 'J', 'N', 'F', 'L', 'W', 'C', 'S'],
    ['W', 'J', 'L', 'T', 'P', 'M', 'S', 'H'],
    ['B', 'C', 'W', 'G', 'F', 'S'],
    ['H', 'T', 'P', 'M', 'Q', 'B', 'W'],
    ['F', 'S', 'W', 'T'],
    ['N', 'C', 'R']
]

def moveCrate(q, o, d):
    for i in range(q):
        popped = stack[o-1].pop()
        stack[d-1].append(popped) 

with open('moves', 'r') as c:
    moves = c.read().splitlines()
    for move in moves:
        splitted = move.split()
        q, o, d = int(splitted[1]), int(splitted[3]), int(splitted[5])
        moveCrate(q, o, d)

solution = ''.join([x[-1] for x in stack])
print(solution)

