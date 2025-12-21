n, d = map(int, input().split())
t1, t2, t3 = map(int, input().split())
dic = {i: False for i in range(n + 1)}
dic[t1] = dic[t2] = dic[t3] = True
for _ in range(d):
    s = set()
    for k, v in dic.items():
        if v:
            s.add(k - 1)
            s.add(k + 1)
    for i in s:
        if 1 <= i <= n:
            dic[i] = True
print(list(dic.values()).count(True))