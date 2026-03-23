a1 = list(map(int, input().split()))
x, y = min(10 * a1[0] + a1[1], 10 * a1[2] + a1[3]), max(10 * a1[0] + a1[1], 10 * a1[2] + a1[3])
a2 = list(map(int, input().split()))
x1, y1 = min(10 * a2[0] + a2[1], 10 * a2[2] + a2[3]), max(10 * a2[0] + a2[1], 10 * a2[2] + a2[3])
a3 = list(map(int, input().split()))
x2, y2 = min(10 * a3[0] + a3[1], 10 * a3[2] + a3[3]), max(10 * a3[0] + a3[1], 10 * a3[2] + a3[3])
result = []
if x1 >= x + 10 and y1 >= y:
    result.append([1, x1, y1])
if x2 >= x + 10 and y2 >= y:
    result.append([2, x2, y2])
if not result:
    print(0)
elif len(result) == 1:
    idx, rx, ry = result[0]
    print(f'{idx}\n{rx // 10}.{rx % 10} {ry // 10}.{ry % 10}')
else:
    result.sort(key=lambda col: col[1])
    idx, rx, ry = result[0]
    print(f'{idx}\n{rx // 10}.{rx % 10} {ry // 10}.{ry % 10}')