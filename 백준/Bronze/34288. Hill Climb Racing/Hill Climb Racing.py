l, a = map(int, input().split())
h = list(map(int, input().split()))
result = 'POSSIBLE'
for i in range(l):
    if h[i + 1] - h[i] > a:
        result = 'BUG REPORT'
        break
print(result)