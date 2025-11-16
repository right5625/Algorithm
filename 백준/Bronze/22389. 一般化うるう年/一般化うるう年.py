while True:
    n, l, r = map(int, input().split())
    if n == l == r == 0:
        break
    A = [0] + [int(input()) for _ in range(n)]
    result = 0
    for x in range(l, r + 1):
        flag = False
        for i in range(1, n + 1):
            if x % A[i] == 0:
                flag = True
                if i % 2 == 1:
                    result += 1
                break
        if not flag and n % 2 == 0:
            result += 1
    print(result)