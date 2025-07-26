import sys
input = lambda: sys.stdin.readline().rstrip()

while True:
    a = list(map(int, input().split()))
    if set(a) == {0}:
        break
    print('yes' if len(set(a)) == 1 or (len(set(a)) == 2 and set([a.count(i) for i in set(a)]) == {4, 8}) or (len(set(a)) == 3 and set([a.count(i) for i in set(a)]) == {4}) else 'no')