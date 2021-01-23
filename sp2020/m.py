def ints(): return [int(x.strip()) for x in input().split()]

R, C = ints()
board = []
for r in range(R):
    board.append(list(input().strip()))

WATER = '*'
EMPTY = '.'
WALL = 'o'

q = [] 
for r in range(R):
    for c in range(C):
        if board[r][c] == WATER:
            q.append((r,c))

seen = set() 

while q:
    pos = q.pop()
    if pos in seen: continue
    r, c = pos

    def go(r, c):
        q.append((r,c))
        board[r][c] = WATER

    if board[r+1][c] == EMPTY:
        go(r+1, c)
    elif board[r+1][c] == WALL:
        if board[r][c-1] == EMPTY:
            go(r, c-1)
        if board[r][c+1] == EMPTY:
            go(r, c+1)

for r in board:
    print(''.join(r))
