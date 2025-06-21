input()
print(*[sorted(i)[1] for i in list(zip(*[list(map(int, input().split())) for _ in range(3)]))])