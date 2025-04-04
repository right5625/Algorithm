import math

A, B, C = map(int, input().split())
T = int(input())
print(A + math.ceil((T - 30) / B) * C if T > 30 else A)