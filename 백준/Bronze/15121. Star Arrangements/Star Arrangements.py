import math

S = int(input())
print(f'{S}:')
for i in range(2, math.ceil(S / 2) + 1):
    for j in range(i - 1, i + 1):
        if S % (i + j) in [0, i]:
            print(f'{i},{j}')