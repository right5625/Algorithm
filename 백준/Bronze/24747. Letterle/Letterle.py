S1 = input()
for i in range(7):
    S2 = input()
    if S2 == S1:
        print('WINNER')
        break
    if i == 6:
        print('LOSER')
        break
    result = ''
    for j in range(5):
        if S2[j] == S1[j]:
            result += 'G'
        elif S2[j] in S1:
            result += 'Y'
        else:
            result += 'X'
    print(result)