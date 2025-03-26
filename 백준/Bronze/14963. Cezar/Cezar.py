from collections import defaultdict

dic = defaultdict(int)
for i in [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]:
    dic[i] += 4
X = 21
for _ in range(int(input())):
    n = int(input())
    dic[n] -= 1
    X -= n
print('VUCI' if sum(dic[i] for i in range(X + 1)) > sum(dic[i] for i in range(X + 1, 12)) else 'DOSTA')