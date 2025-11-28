N, M = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(N)]
print(sum([max(i) for i in list(zip(*G))]))