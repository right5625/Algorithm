from itertools import permutations

result = float('inf')
for i, j, k in permutations(list(map(int, input().split())), 3):
    if len(str(int(str(i) + str(j) + str(k)))) == 3:
        result = min(result, int(str(i) + str(j) + str(k)))
print(result)