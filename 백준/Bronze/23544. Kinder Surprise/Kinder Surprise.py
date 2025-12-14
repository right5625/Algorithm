n = int(input())
print(n - len(set(input() for _ in range(n))))