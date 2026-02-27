from math import ceil

dic = {'S': 6, 'M': 8, 'L': 12}
cur = {'S': 0, 'M': 0, 'L': 0}
for _ in range(int(input())):
    s, l = input().split()
    cur[s] += int(l)
print(sum(ceil(cur[i] / dic[i]) for i in 'SML'))