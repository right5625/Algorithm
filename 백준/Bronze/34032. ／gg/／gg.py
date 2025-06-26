from math import ceil

N = int(input())
S = input()
print('Yes' if S.count('O') >= ceil(N / 2) else 'No')