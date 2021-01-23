def ints(): return [int(x.strip()) for x in input().split()]

def solve():

    F = ints()[0] 
    P = ints()[0]

    from collections import defaultdict

    outgoing = defaultdict(list)

    for i in range(P):
        a, b = ints() 
        outgoing[a].append(b)

    num_incoming = {k: 0 for k in range(1, F+1)}

    for fr, to in outgoing.items():
        for t in to:
            num_incoming[t] += 1

    # print(outgoing)
    # print(num_incoming)

    topo = [] 
    q = [k for k, v in num_incoming.items() if v == 0]
    while q:
        x = q.pop()
        topo.append(x)
        for y in outgoing[x]:
            num_incoming[y] -= 1
            if num_incoming[y] == 0:
                q.append(y)
    # print(topo)

    if len(topo) != len(num_incoming):
        return -1

    max_len = defaultdict(int)

    for x in topo:
        l = max_len[x]
        for y in outgoing[x]:
            max_len[y] = max(max_len[y], 1 + l)
    return max(max_len.values()) + 1

if __name__ == "__main__":
    print(solve())