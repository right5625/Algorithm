c1, m1 = map(int, input().split())
c2, m2 = map(int, input().split())
c3, m3 = map(int, input().split())
lst = [m1, m2, m3]
for i in range(100):
    if i % 3 == 0:
        if lst[0] + lst[1] >= c2:
            lst[0] -= c2 - lst[1]
            lst[1] = c2
        else:
            lst[1] = lst[0] + lst[1]
            lst[0] = 0
    elif i % 3 == 1:
        if lst[1] + lst[2] >= c3:
            lst[1] -= c3 - lst[2]
            lst[2] = c3
        else:
            lst[2] = lst[1] + lst[2]
            lst[1] = 0
    else:
        if lst[2] + lst[0] >= c1:
            lst[2] -= c1 - lst[0]
            lst[0] = c1
        else:
            lst[0] = lst[2] + lst[0]
            lst[2] = 0
print(*lst, sep='\n')