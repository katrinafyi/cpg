def ints():
    return tuple(int(x) for x in input().split())

def read_tree(lines, f=lambda x: x):
    tree = {}
    for i in range(lines):
        tree[f(i)] = tuple(f(x) for x in ints()[1:])
    return tree

from collections import defaultdict

def reduce(tree):
    # F = final states
    # Q = all states
    by_children = defaultdict(set)
    for x, cs in tree.items():
        by_children[len(cs)].add(x)

    P = set(map(frozenset, by_children.values()))
    W = set(P)

    incoming_nodes = defaultdict(lambda: [set(), set(), set(), set()])
    for parent, children in tree.items():
        for i, c in enumerate(children):
            incoming_nodes[c][i].add(parent)
    # print(incoming_nodes)

    # return 2
    while W:
        A = next(iter(W))
        W.remove(A)
        for i in range(4):
            X = set()
            for a in A:
                X.update(incoming_nodes[a][i])

            for Y in tuple(P):
                x = X & Y
                y = Y - X
                if not (x and y):
                    continue

                x = frozenset(x)
                y = frozenset(y)
                P.remove(Y)
                P.add(x)
                P.add(y)

                if Y in W:
                    W.remove(Y)
                    W.add(x)
                    W.add(y)
                else:
                    if len(x) <= len(y):
                        W.add(x)
                    else:
                        W.add(y)

    return P
    
def mapping(reduction):
    m = {}
    for nodes in reduction:
        for x in nodes:
            m[x] = nodes
    return m

def compare(left_tree, right_tree, left_map, right_map, left, right, seen=None):
    if seen is None:
        seen = set()

    if left_map[left] in seen:
        return True
    

def main():
    while 1:
        num_left, num_right = ints()
        if num_left == num_right == 0: break
        left = read_tree(num_left)
        right = read_tree(num_right, lambda x: -x-1)
        # left.update(right)
        left_map = mapping(reduce(left))
        right_map = mapping(reduce(right))
        # print(left_map, right_map)

        left2right = {}
        seen = set()
        def equal(left_node, right_node):
            left_group = left_map[left_node]
            right_group = right_map[right_node]

            if (left_group in seen) != (right_group in seen):
                return False
            elif left_group in seen:
                return True
            
            left_children = left[left_node]
            right_children = right[right_node]

            if len(left_children) != len(right_children):
                return False

            seen.add(left_group)
            seen.add(right_group)
            left2right[left_group] = right_group

            for c1, c2 in zip(left_children, right_children):
                if not equal(c1, c2): return False

            return True



        result = equal(0, -1)
        print('YES' if result else 'NO')
        input()

if __name__ == "__main__":
    main()