t = list(map(float, input().split()))
avg = sum(t) / 10
s = (sum((i - avg) ** 2 for i in t) / 9) ** 0.5
print('NOT COMFY' if s > 1 else 'COMFY')