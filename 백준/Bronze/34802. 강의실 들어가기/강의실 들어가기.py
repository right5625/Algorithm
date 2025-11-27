h1, m1, s1 = map(int, input().split(':'))
h2, m2, s2 = map(int, input().split(':'))
t, k = map(int, input().split())
print(1 if (h2 * 3600 + m2 * 60 + s2) - (h1 * 3600 + m1 * 60 + s1) >= t * (100 - k) // 100 else 0)