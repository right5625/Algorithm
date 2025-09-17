N = int(input())
A = list(map(lambda x: x[0], sorted({i: j for i, j in zip(range(N), list(map(int, input().split())))}.items(), key=lambda x: x[1])))
result = [0] * N
for i in range(N):
    result[A[i]] = i + 1
print(*result)