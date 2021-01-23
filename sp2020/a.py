def ints(): return [int(x.strip()) for x in input().split()]

N = int(input() )

fib = [0, 1, 1, 2, 3, 5, 8, 13]

for i in range(1, N + 1):
    print('fizz' if i in fib else 'buzz', end='')
print()

