from math import ceil

while True:
    N = int(input())
    if N == 0:
        break
    result = 0
    l, r, s = 1, 2, 3
    while l < r <= ceil(N / 2):
        if s < N:
            r += 1
            s += r
        else:
            if s == N:
                result += 1
            s -= l
            l += 1
    print(result)