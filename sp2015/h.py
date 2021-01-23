def ints():
    return [int(x) for x in input().strip().split()]

shifts = [
    (-1, 0),
    (0, -1),
    (1, 0),
    (0, 1)
]

INF = float('inf')

def main():
    # width, height
    cols, rows = ints() 
    n = cols * rows

    def to_i(r, c):
        return r * cols + c

    d = [[INF] * n for _ in range(n)]
    for dr, dc in shifts:
        for r in range(rows):
            for c, dist in enumerate(ints()):
                if not (0 <= r+dr < rows and 0 <= c+dc < cols): continue
                # print(r, c, dist)
                d[to_i(r, c)][to_i(r+dr, c+dc)] = dist

    print(d)
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # if not (0 <= r+dr < rows and 0 <= c+dc < cols): continue
                new_d = d[i][k] + d[k][j]

                if new_d < d[i][j]:
                    d[i][j] = new_d

    s = 0 
    for i in range(n):
        for j in range(n):
            if i == j: continue
            s += d[i][j]
    
    from math import ceil
    print(ceil(s / n))
    print(d)

if __name__ == "__main__":
    main()