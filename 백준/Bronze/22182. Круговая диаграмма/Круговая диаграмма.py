from math import pi

n, r = map(int, input().split())
a = list(map(int, input().split()))
for i in a:
    print((r * r * pi) * (i / sum(a)))