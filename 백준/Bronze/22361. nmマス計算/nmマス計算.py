while True:
    n, m = map(int, input().split())
    if n == m == 0:
        break
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    result = [0] * 10
    for i in a:
        for j in b:
            for k in str(i * j):
                result[int(k)] += 1
    print(*result)