from collections import defaultdict

input()
dic = defaultdict(int)
for i in list(map(int, input().split())):
    dic[i] += 1
print('Yes' if len(set(dic.values()) - {1, 2}) == 0 else 'No')