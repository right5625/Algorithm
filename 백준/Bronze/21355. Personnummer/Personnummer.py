S = input()
if '-' in S:
    A = 20
    sep = '-'
else:
    A = 19
    sep = '+'
print(str(A if int(S[:2]) < 20 else A - 1) + ''.join(S.split(sep)))