n, m = map(int, input().split())
s = list(input().split())
s = [s[-1]] + s[:-1]
t = list(input().split())
t = [t[-1]] + t[:-1]
for _ in range(int(input())):
    y = int(input())
    print(s[y % n] + t[y % m])