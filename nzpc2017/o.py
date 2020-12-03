from collections import defaultdict
from functools import total_ordering

@total_ordering
class Query:
    low: int 
    high: int
    i: int

    def __init__(self, low, high, i):
        self.low = low 
        self.high = high 
        self.i = i

    def __eq__(self, other):
        return self.low == other.low and self.high == other.high

    def __lt__(self, other):
        if self.low != other.low:
            return self.low < other.low
        return self.high < other.high

def solve(skills, queries, target):
    # sorts by low then high
    queries.sort()

    low = queries[0].low
    high = queries[0].high

    freq = defaultdict(int)
    teams = 0

    def add_skill(i):
        nonlocal teams

        this = skills[i]
        other = target - this

        freq[this] += 1
        if freq[other] >= freq[this]:
            teams += 1

    def remove_skill(i):
        nonlocal teams

        this = skills[i]
        other = target - this

        if freq[this] == freq[other]:
            teams -= 1
        freq[this] -= 1

    for i in range(low, high + 1):
        add_skill(i)

    answers = [None] * len(queries)
    for q in queries:
        # print(q)
        # print(low, high)
        while high > q.high:
            remove_skill(high)
            high -= 1
            # print('high down')
            # print(freq)

        while low < q.low:
            remove_skill(low)
            low += 1
            # print('low up')
            # print(freq)

        while high < q.high:
            high += 1
            add_skill(high)
            # print('high up')
            # print(freq)

        # while low > q.low:
        #     low -= 1
        #     add_skill(low)

        assert low == q.low
        assert high == q.high
        # print(low, high)
        answers[q.i] = teams

    return answers




def ints():
    return [int(x) for x in input().split()]

def main():
    num_students, num_queries, target = ints() 
    if num_students == 0: return False
    skills = ints()

    queries = [] 
    for i in range(num_queries):
        low, high = ints()
        queries.append(Query(low - 1, high - 1, i))

    for x in solve(skills, queries, target):
        print(x) 
    print()
    return True

if __name__ == "__main__":
    while main():
        pass