while True:
    m, n = map(int, input().split())
    if m == n == 0:
        break
    A = list(map(int, input().split()))
    res = 0
    for _ in range(n):
        flag = True
        for i, j in enumerate(list(map(int, input().split()))):
            if A[i] < j:
                flag = False
                break
        if flag:
            res += 1
    print(res)