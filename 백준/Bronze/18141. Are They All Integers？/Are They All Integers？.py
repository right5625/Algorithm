from itertools import permutations

input()
result = 'yes'
for i, j, k in permutations(list(map(int, input().split())), 3):
    if (i - j) / k != (i - j) // k:
        result = 'no'
        break
print(result)