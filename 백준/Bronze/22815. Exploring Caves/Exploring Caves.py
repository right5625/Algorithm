for _ in range(int(input())):
    lst = [[0, 0]]
    cur_x = cur_y = 0
    while True:
        dx, dy = map(int, input().split())
        if dx == dy == 0:
            break
        cur_x += dx
        cur_y += dy
        lst.append([cur_x, cur_y])
    print(*sorted([[(x ** 2 + y ** 2) ** 0.5, x, y] for x, y in lst], key=lambda x: (-x[0], -x[1]))[0][1:])