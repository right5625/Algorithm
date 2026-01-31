from itertools import permutations

M, N = map(int, input().split())
t = sorted(list(map(int, input().split())))
result = 4
for i in permutations(t):
    cur_weight, cur_cnt, tot = 0, 0, 1
    for j in i:
        if cur_cnt + 1 <= M and cur_weight + j <= N:
            cur_weight += j
            cur_cnt += 1
        else:
            tot += 1
            cur_weight = j
            cur_cnt = 1
    result = min(result, tot)
print(result)