from itertools import combinations

for _ in range(int(input())):
    a = list(map(int, input().split()))
    result = [0, 0, 0]
    for i in combinations(a, 3):
        s = sorted(i)
        if s[0] + s[1] > s[2]:
            if s[0] ** 2 + s[1] ** 2 > s[2] ** 2:
                result[1] += 1
            elif s[0] ** 2 + s[1] ** 2 < s[2] ** 2:
                result[2] += 1
            else:
                result[0] += 1
    print(*result)