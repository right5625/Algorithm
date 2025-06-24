x1, x2, x3 = map(int, input().split())
if max(x1, x2, x3) * 2 == sum([x1, x2, x3]):
    print(0)
else:
    flag = False
    for i in range(3):
        x = [x1, x2, x3]
        x = [x.pop(i)] + x
        if abs(x[1] - x[2]) <= x[0] and abs(x[1] - x[2]) % 2 == x[0] % 2:
            rem = x[0] - abs(x[1] - x[2])
            print(f'{i + 1}\n{abs(x[1] - x[2]) + rem // 2} {rem // 2}')
            flag = True
            break
    if not flag:
        print(-1)