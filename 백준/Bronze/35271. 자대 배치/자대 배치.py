N, M = map(int, input().split())
A = [0] + list(map(int, input().split()))
result = []
for _ in range(N):
    flag = False
    for i in list(map(int, input().split())):
        if A[i]:
            A[i] -= 1
            result.append(i)
            flag = True
            break
    if not flag:
        result.append(-1)
print(*result)