t = list(map(float, input().split()))
print('NOT COMFY' if (sum((i - sum(t) / 10) ** 2 for i in t) / 9) ** 0.5 > 1 else 'COMFY')