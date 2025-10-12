input()
h, m = map(int, input().split(':'))
a1 = input()
a2 = int(input())
a3 = int(input())
a4 = int(input())
t = h * 60 + m
if a1 in ['sat', 'sun']:
    t *= 2
if a2:
    t *= 2
if a3:
    t *= 3
if a4:
    t *= 3
print(f'{t // 60}:{t % 60:02d}')