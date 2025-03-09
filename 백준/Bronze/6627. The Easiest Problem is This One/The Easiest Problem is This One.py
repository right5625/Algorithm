while True:
    N = input()
    if N == '0':
        break
    S = sum(map(int, N))
    p = 11
    while True:
        if S == sum(map(int, str(int(N) * p))):
            print(p)
            break
        p += 1