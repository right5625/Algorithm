n = int(input())
p = list(map(int, input().split()))
result = 0
for i in range(1, n):
    if p[0] >= p[i]:
        result = i
        break
print(result if result != 0 else 'infinity')