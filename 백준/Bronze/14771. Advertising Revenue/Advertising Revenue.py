for t in range(1, int(input()) + 1):
    n, v = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(n)]
    res = 0
    for _ in range(v):
        a1, a2, c = map(int, input().split())
        if lst[a1 - 1][0] == 1:
            res += lst[a1 - 1][1]
        if lst[a2 - 1][0] == 1:
            res += lst[a2 - 1][1]
        if lst[a1 - 1][0] == 0 and c == 1:
            res += lst[a1 - 1][1]
        elif lst[a2 - 1][0] == 0 and c == 2:
            res += lst[a2 - 1][1]
    print(f'Data Set {t}:\n{res}\n')