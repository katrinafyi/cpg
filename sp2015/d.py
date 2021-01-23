def ints():
    return [int(x) for x in input().rstrip().split()]

def main():
    num_left, num_right = ints() 
    obstacles_left = [ints() for x in range(num_left)]
    obstacles_right = [ints() for x in range(num_right)]

    table = []
    

    print(obstacles_left)
    print(obstacles_right)

if __name__ == "__main__":
    main()
