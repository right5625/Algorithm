n, x, m = map(int, input().split())
box = [0] * (n + 1)
for _ in range(m):
    box[int(input())] += 1
print(min(sum([box[i] for i in range(1, x)]), sum([box[i] for i in range(x, n + 1)])))