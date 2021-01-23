line, n = input().strip().split()
n = int(n)

num_splits = n 
from math import ceil 
len_split = ceil(len(line) / num_splits)


line = line.ljust(num_splits * len_split, 'X')
# print(line)

x = []
for i in range(len(line)):
    chunk = i % num_splits
    j = chunk*len_split + i // num_splits
    # print(j)
    x.append(line[j])
print(''.join(x))