t = int(input())
n, a, b, c = map(int, input().split())
print(max(a + b + c - n * 2, 0) if t == 1 else min(a, b, c))