# 기하(CCW)
def CCW(x1, y1, x2, y2, x3, y3):
    return (x1 * y2 + x2 * y3 + x3 * y1) - (y1 * x2 + y2 * x3 + y3 * x1)

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
ABC = CCW(x1, y1, x2, y2, x3, y3)
ABD = CCW(x1, y1, x2, y2, x4, y4)
CDA = CCW(x3, y3, x4, y4, x1, y1)
CDB = CCW(x3, y3, x4, y4, x2, y2)
if ABC * ABD == 0 and CDA * CDB == 0:
    if min(x1, x2) <= max(x3, x4) and min(x3, x4) <= max(x1, x2) and min(y1, y2) <= max(y3, y4) and min(y3, y4) <= max(y1, y2):
        print(1)
    else:
        print(0)
elif ABC * ABD <= 0 and CDA * CDB <= 0:
    print(1)
else:
    print(0)