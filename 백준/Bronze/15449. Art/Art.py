from itertools import combinations

res = 0
for i in combinations(map(int, input().split()), 3):
    if i[0] + i[1] > i[2] and i[1] + i[2] > i[0] and i[2] + i[0] > i[1]:
        res += 1
print(res)