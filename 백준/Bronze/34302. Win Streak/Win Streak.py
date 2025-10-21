import sys
input = lambda: sys.stdin.readline().rstrip()

cur = result = 0
for _ in range(int(input())):
    S, T = map(int, input().split())
    if S > T:
        cur += 1
    else:
        result = max(result, cur)
        cur = 0
print(max(result, cur))