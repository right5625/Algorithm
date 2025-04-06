while True:
    N = int(input())
    if N == 0:
        break
    S = ''.join(input().split())
    res = 0
    for i in range(N - 3):
        if S[i:i + 4] == '2020':
            res += 1
    print(res)