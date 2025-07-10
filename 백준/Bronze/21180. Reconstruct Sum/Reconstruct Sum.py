import sys
input = lambda: sys.stdin.readline().rstrip()

lst = [int(input()) for _ in range(int(input()))]
print(int(sum(lst) / 2) if sum(lst) / 2 in lst else 'BAD')