# 기하(CCW)
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
CCW = (x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3)
if not CCW:
    print(0)
else:
    print(1 if CCW > 0 else -1)