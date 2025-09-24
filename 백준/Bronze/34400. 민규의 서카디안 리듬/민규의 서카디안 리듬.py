import sys
input = lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):
    print('ONLINE' if int(input()) % 25 < 17 else 'OFFLINE')