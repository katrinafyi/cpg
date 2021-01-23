def solve():

    def ints():
        return [int(x.strip()) for x in input().split()]

    N, D = ints() 
    lights = []
    for _ in range(N):
        lights.append(ints())

    lights.sort() 

    t = 0 
    d = 0 
    for light in lights:
        x, a, g, r = light
        # move to this traffic light
        t += x - d
        d = x

        if t < a:
            return False # arrived before first green
        c = g + r # cycle length
        j = (t - a) % c
        if j <= g:
            continue
        else:
            return False # hit red part
    
    return True


if __name__ == "__main__":
    print('YES' if solve() else 'NO')