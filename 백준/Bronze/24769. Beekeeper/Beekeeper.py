while True:
    N = int(input())
    if N == 0:
        break
    result, cnt = '', 0
    for _ in range(N):
        S = input()
        cur_cnt = S.count('aa') + S.count('ee') + S.count('ii') + S.count('oo') + S.count('uu') + S.count('yy')
        if cur_cnt >= cnt:
            result = S
            cnt = cur_cnt
    print(result)