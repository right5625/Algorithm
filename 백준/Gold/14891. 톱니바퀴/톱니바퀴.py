from collections import deque

def spin1(n):
    T[n].appendleft(T[n].pop())

def spin2(n):
    T[n].append(T[n].popleft())

T = [[]]
for _ in range(4):
    T.append(deque(input()))
for _ in range(int(input())):
    n, d = map(int, input().split())
    flag = False
    for i in range(n, 1, -1):
        if T[i - 1][2] == T[i][6]:
            left = i
            flag = True
            break
    if not flag:
        left = 1
    flag = False
    for i in range(n, 4):
        if T[i][2] == T[i + 1][6]:
            right = i
            flag = True
            break
    if not flag:
        right = 4
    if d == 1:
        spin1(n)
        d = -1
    else:
        spin2(n)
        d = 1
    s = d
    for i in range(n - 1, left - 1, -1):
        if d == 1:
            spin1(i)
            d = -1
        else:
            spin2(i)
            d = 1
    d = s
    for i in range(n + 1, right + 1):
        if d == 1:
            spin1(i)
            d = -1
        else:
            spin2(i)
            d = 1
res = 0
for i in range(1, 5):
    if T[i][0] == '1':
        res += 2 ** (i - 1)
print(res)