x1, x2, x3 = map(int, input().split())
if max(x1, x2, x3) - sum([x1, x2, x3]) == -max(x1, x2, x3):
    print(0)
else:
    if abs(x2 - x3) <= x1 and abs(x2 - x3) % 2 == x1 % 2:
        result1 = result2 = 0
        r = x1
        if x2 < x3:
            result1 = x3 - x2
            r -= x3 - x2
        elif x2 > x3:
            result2 = x2 - x3
            r -= x2 - x3
        result1 += r // 2
        result2 += r // 2
        print(f'1\n{result1} {result2}')
    elif abs(x1 - x3) <= x2 and abs(x1 - x3) % 2 == x2 % 2:
        result1 = result2 = 0
        r = x2
        if x1 < x3:
            result1 = x3 - x1
            r -= x3 - x1
        elif x1 > x3:
            result2 = x1 - x3
            r -= x1 - x3
        result1 += r // 2
        result2 += r // 2
        print(f'2\n{result1} {result2}')
    elif abs(x1 - x2) <= x3 and abs(x1 - x2) % 2 == x3 % 2:
        result1 = result2 = 0
        r = x3
        if x1 < x2:
            result1 = x2 - x1
            r -= x2 - x1
        elif x1 > x2:
            result2 = x1 - x2
            r -= x1 - x2
        result1 += r // 2
        result2 += r // 2
        print(f'3\n{result1} {result2}')
    else:
        print(-1)