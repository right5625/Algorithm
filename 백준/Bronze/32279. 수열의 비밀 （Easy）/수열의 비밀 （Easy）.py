n = int(input())
p, q, r, s = map(int, input().split())
a = [0] + [int(input())]
for i in range(2, n + 1):
    a.append(p * a[i // 2] + q if i % 2 == 0 else r * a[i // 2] + s)
print(sum(a))