for _ in range(int(input())):
    n = int(input())
    scores = [0] * 11
    for _ in range(n):
        b, d = map(int, input().split())
        scores[d] = max(scores[d], b)
    print("MOREPROBLEMS" if 0 in scores[1:] else sum(scores))