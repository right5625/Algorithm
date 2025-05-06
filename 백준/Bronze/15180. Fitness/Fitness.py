S = int(input())
result = [S]
while True:
    s = input()
    if s == '#':
        break
    if s[0] == 'A':
        S -= int(s[1])
        if S < 1:
            S += 8
    else:
        S += int(s[1])
        if S > 8:
            S -= 8
    result.append(S)
if len(set(result)) < 5 or len(result) > len(set(result)):
    result.append('reject')
print(*result)