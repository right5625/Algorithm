N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
result = 0
for i in A:
    for j in B:
        if i <= j:
            result += 1
print(result)