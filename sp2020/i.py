N = int(input())
board = [input().strip() for x in range(N)]

WALL = '#'
EMPTY = '.'

subtree_edges = [[None]*N for i in range(N)]

shifts = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def adjacent(r, c):
    for dr, dc in shifts:
        r2 = r+dr 
        c2 = c+dc
        if not (0 <= r2 < N and 0 <= c2 < N):
            continue
        if board[r2][c2] == WALL: continue
        yield r2, c2

END = (N-1, N-1)

parents = [[None]*N for i in range(N)]

def do_subtree(r, c):
    if (r, c) == END: return 0
    s = 0 
    p = parents[r][c]
    for r2, c2 in adjacent(r, c):
        if (r2, c2) == p: continue
        parents[r2][c2] = r, c
        
        s += 1 + do_subtree(r2, c2)
    subtree_edges[r][c] = s
    return s

do_subtree(0, 0)

# print(subtree_edges)
# print(parents)

prev = None
p = END
d = 0
while p is not None:
    r, c = p
    # print(p)
    if p != END:
        for r2, c2 in adjacent(r, c):
            if (r2, c2) == parents[r][c]: continue
            if (r2, c2) == prev: continue
            # print(r2, c2, subtree_edges[r2][c2])
            d += 2 + 2 * subtree_edges[r2][c2]
    prev = p
    p = parents[r][c]
    d += 1
print(d)


'''

def do_distance(r, c):
    if (r, c) == END: return 1
    d = 0 
    to_end = None
    p = parents[r][c]
    for r2, c2 in adjacent(r, c):
        pos = r2, c2
        if pos == p: continue
        if board[r2][c2] == WALL: continue
        if pos in path_to_end:
            to_end = pos
        else:
            d += 2 * do_distance(r2, c2)
    if to_end:
        d += do_distance(*to_end)
    return d
        

print(do_distance(0, 0))

'''