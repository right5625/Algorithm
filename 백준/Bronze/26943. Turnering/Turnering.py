n, r = map(int, input().split())
a = [i for i in range(1, n + 1)]
a = a[n - r:-1] + a[:n - r] + [a[-1]]
for i in range(n // 2):
    print(f'{a[i]}-{a[-(i + 1)]}')