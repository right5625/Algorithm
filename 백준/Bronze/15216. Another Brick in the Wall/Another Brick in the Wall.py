from collections import deque

h, w, n = map(int, input().split())
x = deque(map(int, input().split()))
wall = deque([w] * h)
res = 'YES'
while wall:
    if wall[0] - x[0] >= 0:
        wall[0] -= x[0]
        if wall[0] == 0:
            wall.popleft()
    else:
        res = 'NO'
        break
    x.popleft()
print(res)