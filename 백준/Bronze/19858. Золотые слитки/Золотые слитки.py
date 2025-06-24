x1, x2, x3 = map(int, input().split())
if max(x1, x2, x3) - sum([x1, x2, x3]) == -max(x1, x2, x3):
    print(0)
else:
    result1 = result2 = 0
    for i in range(3):
        x = [x1, x2, x3]
        x = [x.pop(i)] + x
        if abs(x[1] - x[2]) <= x[0] and abs(x[1] - x[2]) % 2 == x[0] % 2:
            rem = x[0]
            result1 = abs(x[1] - x[2])
            rem -= abs(x[1] - x[2])
            result1 += rem // 2
            result2 += rem // 2
            print(f'{i + 1}\n{result1} {result2}')
            break
    if result1 == result2 == 0:
        print(-1)