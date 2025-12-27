from math import pi

w, h = map(int, input().split())
r = int(input())
print(w * h - ((r * 0.5) ** 2 * pi))