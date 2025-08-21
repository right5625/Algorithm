a = list(map(int, input().split()))
if a.count(0) == 1:
    print(a.index(0) + 1, ({1, 2, 3, 4} - set(a)).pop())
elif a.count(0) == 2:
    print(*sorted(list({1, 2, 3, 4} - set(a))))
else:
    print(*a[:2])