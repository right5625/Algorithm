while True:
    N = int(input())
    if N == 0:
        break
    H = list(map(int, input().split()))
    H = [H[-1]] + H + [H[0]]
    res = 0
    for i in range(1, N + 1):
        if (H[i - 1] < H[i] and H[i] > H[i + 1]) or (H[i - 1] > H[i] and H[i] < H[i + 1]):
            res += 1
    print(res)