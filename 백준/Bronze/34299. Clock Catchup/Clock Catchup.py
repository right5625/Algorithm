h1, m1, s1 = map(int, input().split(':'))
h2, m2, s2 = map(int, input().split(':'))
t1 = h1 * 3600 + m1 * 60 + s1
t2 = h2 * 3600 + m2 * 60 + s2
print(f'{int(t2 / 43200) - int(t1 / 43200)} {int(t2 / 3600) - int(t1 / 3600)} {int(t2 / 60) - int(t1 / 60)}')