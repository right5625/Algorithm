for _ in range(int(input())):
    S = input()
    prev, cnt = S[0], 1
    result = []
    for cur in S[1:]:
        if cur == prev:
            cnt += 1
        else:
            result.append(str(cnt) + ' ' + str(prev))
            prev = cur
            cnt = 1
    result.append(str(cnt) + ' ' + str(prev))
    print(*result)