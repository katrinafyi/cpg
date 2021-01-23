def ints(): return [int(x.strip()) for x in input().split()]

R, C, Y = ints() 

fold_len =  min(Y, C-Y)
if fold_len < Y:
    left_len = Y - fold_len
    right_len = 0 
else:
    left_len = 0 
    right_len = C - 2*fold_len

HOLE = 'o'
WALL = 'x'

def do_fold(base, other):
    x = ''
    assert len(base) == len(other)
    for b, o in zip(base, reversed(other)):
        x += HOLE if (b == HOLE and o == HOLE) else WALL
    return x

# print(R, C, Y)
# print(left_len, fold_len, right_len)

for r in range(R):
    line = input().strip() 
    # print(line)
    if left_len:
        print(line[:left_len], end='')
        print(do_fold(line[left_len : left_len + fold_len], line[left_len + fold_len : left_len + 2*fold_len]))
    else:
        if right_len:
            print(line[-right_len:][::-1], end='')
        print(do_fold(line[0:fold_len], line[fold_len : 2*fold_len]))

