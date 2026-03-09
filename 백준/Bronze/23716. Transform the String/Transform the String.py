for case in range(1, int(input()) + 1):
    S1 = input()
    S2 = input()
    result = 0
    for i in S1:
        cnt = float('inf')
        for j in S2:
            cnt = min(cnt, abs(ord(i) - ord(j)), 26 - abs(ord(i) - ord(j)))
        result += cnt
    print(f'Case #{case}: {result}')