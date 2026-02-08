for _ in range(int(input())):
    n = int(input())
    a = [0] + list(map(int, input().split())) + [1440]
    cnt = 0
    for i in range(n + 1):
        cnt += (a[i + 1] - a[i]) // 120
    print('YES' if cnt >= 2 else 'NO')