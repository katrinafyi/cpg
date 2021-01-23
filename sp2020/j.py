def ints(): return [int(x.strip()) for x in input().split()]

# t is interval of measurement
# d is time considered
# p is percentile required
# r is response delay required for responsiveness
num_meas, t, d, p, r = ints() 
num_attempts = ints() [0]

SUBMIT = 'S'
REPLY = 'R'
MEASURE = 'M'

timeline = [] # list of (time, response time)
submitted = [None] * num_attempts
for i in range(2 * num_attempts):
    a, b, c = input().strip().split() 
    a = int(a)
    b = int(b) - 1 
    if c == SUBMIT:
        submitted[b] = a
    else:
        timeline.append((a, 'R', a - submitted[b]))

# for i in range(1, num_meas + 1):
#     timeline.append((i * t, MEASURE, None))

# timeline.sort()

from collections import deque
from math import ceil, floor

considering = deque()

def measure():
    if not considering: return True
    l = [x[1] for x in considering]
    l.sort() 
    # print(l)
    i = (p/100 * len(l))
    if i == int(i): i = int(i) - 1
    else: i = floor(i)
    return l[i] <= r

# print(num_meas, t, d, p, r)
# print(timeline)

num_responsive = 0
prev_measure = -1
prev_measure_time = 0
changed = True
for time, event, value in timeline:
    if event == REPLY:
        if time > prev_measure_time + t:
            next_measure_time = floor(time / t) * t
            while considering and considering[0][0] < next_measure_time - d:
                considering.popleft()
            m = measure()
            num_responsive += m * (time - prev_measure_time + t) // t
            prev_measure_time = next_measure_time
        considering.append((time, value))
        changed = True

print(num_responsive)