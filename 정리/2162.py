#기하(CCW)
def find(v):
    if union[v] < 0:
        return v
    union[v] = find(union[v])
    return union[v]

def CCW(x1, y1, x2, y2, x3, y3):
    return (x1 * y2 + x2 * y3 + x3 * y1) - (y1 * x2 + y2 * x3 + y3 * x1)

def crose_check(x1, y1, x2, y2, x3, y3, x4, y4):
    ABC = CCW(x1, y1, x2, y2, x3, y3)
    ABD = CCW(x1, y1, x2, y2, x4, y4)
    CDA = CCW(x3, y3, x4, y4, x1, y1)
    CDB = CCW(x3, y3, x4, y4, x2, y2)
    if ABC * ABD == 0 and CDA * CDB == 0:
        if min(x1, x2) <= max(x3, x4) and min(x3, x4) <= max(x1, x2) and min(y1, y2) <= max(y3, y4) and min(y3, y4) <= max(y1, y2):
            return True
        else:
            return False
    elif ABC * ABD <= 0 and CDA * CDB <= 0:
        return True
    else:
        return False

N = int(input())
union = [-1] * (N + 1)
L = [[]]
for i in range(1, N + 1):
    L.append(list(map(int, input().split())))
    for j in range(1, i):
        if crose_check(L[i][0], L[i][1], L[i][2], L[i][3], L[j][0], L[j][1], L[j][2], L[j][3]):
            a = find(i)
            b = find(j)
            if a != b:
                union[a] += union[b]
                union[b] = a
group_cnt = 0
segment_cnt = 0
for i in range(1, N + 1):
    if union[i] < 0:
        group_cnt += 1
        segment_cnt = min(segment_cnt, union[i])
print(group_cnt)
print(-segment_cnt)