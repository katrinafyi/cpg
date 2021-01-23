def ints(): return [int(x.strip()) for x in input().split()]

N = ints()[0]
volumes = ints() 
nums = [input().strip() for x in range(N)]

def mean(x):
    s = sum(x)
    return s/len(x)

print(max(
    (mean([volumes[int(j)] for j in n]), -i, n)
    for i, n in enumerate(nums)
)[-1])