from itertools import permutations

N = int(input())
A = list(map(int, input().split()))
op = list(map(int, input().split()))
P = set(permutations('+' * op[0] + '-' * op[1] + '*' * op[2] + '/' * op[3]))
maxRes, minRes = -float('inf'), float('inf')
for i in P:
    n = A[0]
    idx = 1
    for j in i:
        if j == '+':
            n += A[idx]
        elif j == '-':
            n -= A[idx]
        elif j == '*':
            n *= A[idx]
        else:
            if n < 0 and A[idx] > 0:
                n = -(-n // A[idx])
            else:
                n //= A[idx]
        idx += 1
    maxRes = max(maxRes, n)
    minRes = min(minRes, n)
print(f'{maxRes}\n{minRes}')