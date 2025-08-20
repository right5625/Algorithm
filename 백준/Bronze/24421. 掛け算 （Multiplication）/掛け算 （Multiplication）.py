from itertools import combinations

input()
result = 0
for x, y, z in combinations(list(map(int, input().split())), 3):
    if x * y == z:
        result += 1
print(result)