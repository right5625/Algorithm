input()
cur = 1
for i in list(map(int, input().split())):
    cur = cur * 2 - i
print('error' if cur < 0 else cur % 1000000007)