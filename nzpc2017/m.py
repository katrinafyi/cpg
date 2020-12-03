from collections import deque

def compare(left, right, seen):
    pass 

def ints():
    return tuple(int(x) for x in input().split())

def bfs_compare(left, right):
    seen = set()

    queue = deque(((0, 0), ))
    while queue:
        x, y = queue.pop()
        
        if len(left[x]) != len(right[y]): return False
        if x in seen: continue
        seen.add(x)

        for c1, c2 in zip(left[x], right[y]):
            if len(left[c1]) != len(right[c2]): return False
            queue.append((c1, c2))

    return True

def dfs_compare(left, right):
    seen = set()

    queue = deque(((0, 0), ))
    while queue:
        x, y = queue.pop()
        
        if len(left[x]) != len(right[y]): return False
        if x in seen: continue
        seen.add(x)

        for c1, c2 in zip(left[x], right[y]):
            if len(left[c1]) != len(right[c2]): return False
            queue.appendleft((c1, c2))

    return True


def read_tree(num_lines):
    t = {}
    for i in range(num_lines):
        t[i] = ints()[1:]
    return t

def main():
    while True:
        num_left, num_right = ints()
        if num_left == num_right == 0: break

        left = read_tree(num_left)
        right = read_tree(num_right)
        # print(left)
        # print(right)
        l = (bfs_compare(left, right) and bfs_compare(right, left)
            and dfs_compare(left, right) and dfs_compare(right, left))

        print('YES' if l else 'NO')
        input()

if __name__ == "__main__":
    main()