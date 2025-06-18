N, P = map(int, input().split())
result = 1
for i in range(2, N + 1):
    result = result * i % P
print(result)