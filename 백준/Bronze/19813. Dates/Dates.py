import sys
input = lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):
    S = input()
    if '.' in S:
        d, m, y = map(int, S.split('.'))
    else:
        m, d, y = map(int, S.split('/'))
    print(f'{d:02d}.{m:02d}.{y:04d} {m:02d}/{d:02d}/{y:04d}')