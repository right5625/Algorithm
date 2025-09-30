from math import ceil

X, Y, Z = map(int, input().split())
U, V, W = map(int, input().split())
print(ceil(U / 100) * X + ceil(V / 50) * Y + ceil(W / 20) * Z)