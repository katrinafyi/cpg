N = int(input())
nums = [int(input()) for i in range(N)]
nums.sort() 
if len(nums) == 1:
    print(0)
else:
    m = float('inf')
    for i in range(len(nums) - 1):
        x = nums[i+1] - nums[i]
        if x < m:
            m = x
    print(m)