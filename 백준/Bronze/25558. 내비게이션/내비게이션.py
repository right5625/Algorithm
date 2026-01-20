import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
sx, sy, ex, ey = map(int, input().split())
minDis = float('inf')
for i in range(1, N + 1):
    curXPos, curYPos, curDis = sx, sy, 0
    for _ in range(int(input())):
        x, y = map(int, input().split())
        curDis += abs(curXPos - x) + abs(curYPos - y)
        curXPos, curYPos = x, y
    curDis += abs(ex - curXPos) + abs(ey - curYPos)
    if curDis < minDis:
        minDis = curDis
        result = i
print(result)