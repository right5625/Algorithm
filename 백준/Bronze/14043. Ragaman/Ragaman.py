from collections import defaultdict

dic1 = defaultdict(int)
dic2 = defaultdict(int)
for i, j in zip(input(), input()):
    dic1[i] += 1
    dic2[j] += 1
for k in dic1.keys():
    dic1[k] -= dic2[k]
print('N' if len(list(filter(lambda x: x < 0, dic1.values()))) or sum(list(dic1.values())) != dic2['*'] else 'A')