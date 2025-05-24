# 큐, 덱
import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

for _ in range(int(input())):
    p = input()
    n = int(input())
    deq = deque(list(filter(None, list(input()[1:-1].split(',')))))
    front = True
    flag = True
    for i in p:
        if i == 'R':
            front = not front
        else:
            try:
                if front:
                    deq.popleft()
                else:
                    deq.pop()
            except:
                flag = False
                break
    if not front:
        deq.reverse()
    print('[' + ','.join(deq) + ']' if flag else 'error')