import sys
input = lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):
    S, n, f, m = map(int, input().split())
    print('YES' if n <= S - m <= n * f else 'NO')