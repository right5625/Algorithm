S = list(input())
for _ in range(int(input())):
    s = list(input())
    if set(S) & set(s) == set(s) and len(s) >= 4 and S[0] in s:
        print(''.join(s))