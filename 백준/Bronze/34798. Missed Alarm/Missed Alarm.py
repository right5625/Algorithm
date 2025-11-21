h1, m1 = map(int, input().split(':'))
h2, m2 = map(int, input().split(':'))
print('YES' if h1 * 60 + m1 < h2 * 60 + m2 else 'NO')