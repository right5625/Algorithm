input()
result = ''
for i, j in zip(input(), input()):
    if i == j:
        if i == 'R':
            result += 'P'
        elif i == 'S':
            result += 'R'
        else:
            result += 'S'
    else:
        if i + j in ('RS', 'SR'):
            result += 'R'
        elif i + j in ('SP', 'PS'):
            result += 'S'
        else:
            result += 'P'
print(result)