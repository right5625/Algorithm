n = int(input())
a = int(input())
b = int(input())
board = [['.' for _ in range(n)] for _ in range(n)]
k = (n - 1) // 2
for y in range(n):
    length_y = abs(k - y)
    if length_y > b:
        continue
    for x in range(n):
        length_x = abs(k - x)
        length = length_x + length_y
        if a <= length <= b:
            board[y][x] = '*'
print('\n'.join(''.join(row) for row in board))