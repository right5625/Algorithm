from itertools import permutations

c1, c2, c3, c4 = input().split()
result = 0
for i in permutations([c1, c2, c3, c4]):
    result = max(result, int(''.join(i)))
print(result)