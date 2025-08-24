import sys
input = lambda: sys.stdin.readline().rstrip()

a, b, c = map(int, input().split())
board = [i for i in range(101)]
for _ in range(b):
    s, e = map(int, input().split())
    board[s] = e
player = [1 for i in range(a + 1)]
turn = 1
for _ in range(c):
    roll = int(input())
    current = player[turn]
    next_pos = min(current + roll, 100)
    next_pos = board[next_pos]
    player[turn] = next_pos
    if next_pos == 100:
        break
    turn += 1
    if turn > a:
        turn = 1
for i in range(1, a + 1):
    print(f'Position of player {i} is {player[i]}.')