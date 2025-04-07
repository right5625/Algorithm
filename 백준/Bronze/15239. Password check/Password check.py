import string

for _ in range(int(input())):
    N = int(input())
    S = input()
    flag1 = False
    for i in string.ascii_lowercase:
        if i in S:
            flag1 = True
            break
    flag2 = False
    for i in string.ascii_uppercase:
        if i in S:
            flag2 = True
            break
    flag3 = False
    for i in string.digits:
        if i in S:
            flag3 = True
            break
    flag4 = False
    for i in '+_)(*&^%$#@!./,;{}':
        if i in S:
            flag4 = True
            break
    print('valid' if flag1 and flag2 and flag3 and flag4 and N >= 12 else 'invalid')