ED, S = input().split()
result = ''
if ED == 'E':
    prev, cnt = S[0], 1
    for i in S[1:]:
        if prev != i:
            result += prev + str(cnt)
            cnt = 0
        prev = i
        cnt += 1
    result += prev + str(cnt)
else:
    for i in range(0, len(S), 2):
        result += S[i] * int(S[i + 1])
print(result)