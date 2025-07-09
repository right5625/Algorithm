S = input()
A, sep = ((20, '-') if '-' in S else (19, '+'))
print(str(A if int(S[:2]) < 20 else A - 1) + ''.join(S.split(sep)))