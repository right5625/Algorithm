l, h, p, e, n = map(int, input().split())
dic = {i: [0, 0] for i in ['Lab', 'Hw', 'Proj', 'Exam']}
for _ in range(n):
    c, i, rs = input().split()
    r, s = map(int, rs.split('/'))
    dic[c][0] += r
    dic[c][1] += s
print(int(sum(i * (j[0] / j[1]) for i, j in zip([l, h, p, e], dic.values()))))