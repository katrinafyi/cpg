def ints(): return [int(x.strip()) for x in input().split()]

N = ints()[0]

people = [ints() for i in range(N)]

distances = []

for i in range(N):
    for j in range(N):
        if i <= j: continue
        x = people[i]
        y = people[j]
        d = (x[0]-y[0])**2 + (x[1]-y[1])**2
        distances.append((d, i, j))

# print(distances)
distances.sort()

paired = set() 
for d, i, j in distances:
    if i not in paired and j not in paired:
        paired.add(i)
        paired.add(j)
    else:
        print(d)
        break