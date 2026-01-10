import string

for case in range(1, int(input()) + 1):
    input()
    S = input()
    upper = lower = digit = special = False
    for i in S:
        if i in string.ascii_uppercase:
            upper = True
        elif i in string.ascii_lowercase:
            lower = True
        elif i in string.digits:
            digit = True
        else:
            special = True
    if not upper:
        S += 'A'
    if not lower:
        S += 'a'
    if not digit:
        S += '0'
    if not special:
        S += '#'
    if len(S) < 7:
        S += 'A' * (7 - len(S))
    print(f'Case #{case}: {S}')