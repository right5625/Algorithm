while True:
    n = int(input())
    if n == 0:
        break
    a = list(map(int, input().split()))
    avg, res = sum(a) / n, 0
    for i in a:
        if i <= avg:
            res += 1
    print(res)