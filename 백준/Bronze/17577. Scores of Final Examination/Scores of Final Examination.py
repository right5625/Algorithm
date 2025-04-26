while True:
    n, m = map(int, input().split())
    if n == m == 0:
        break
    scores = [0] * n
    for _ in range(m):
        for i, j in enumerate(list(map(int, input().split()))):
            scores[i] += j
    print(max(scores))