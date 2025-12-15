from collections import defaultdict

input()
dic = defaultdict(int)
for i in list(map(int, input().split())):
    dic[i] += 1
print(sorted(dic.items(), key=lambda x: (x[1], x[0]))[0][0])