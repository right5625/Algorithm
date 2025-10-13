for _ in range(int(input())):
    k, n = map(int, input().split())
    print(*[(i + k) % 10 for i in list(map(int, str(n)))], sep='')