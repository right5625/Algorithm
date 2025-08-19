N, M = map(int, input().split())
result = [i for i in range(N + 1)]
for _ in range(M):
    X, Y = map(int, input().split())
    result[X] = Y
print(*result[1:], sep='\n')