def game():
    dr = [1, 1, 0, -1]
    dc = [0, 1, 1, 1]
    for r in range(19):
        for c in range(19):
            if board[r][c]:
                for i in range(4):
                    mr, mc = r + dr[i], c + dc[i]
                    cnt = 1
                    while 0 <= mr < 19 and 0 <= mc < 19 and board[r][c] == board[mr][mc]:
                        cnt += 1
                        if cnt == 5:
                            if 0 <= mr + dr[i] < 19 and 0 <= mc + dc[i] < 19 and board[r][c] == board[mr + dr[i]][mc + dc[i]]:
                                break
                            if 0 <= r - dr[i] < 19 and 0 <= c - dc[i] < 19 and board[r][c] == board[r - dr[i]][c - dc[i]]:
                                break
                            return board[r][c], r + 1, c + 1
                        mr += dr[i]
                        mc += dc[i]
    return 0

board = [list(map(int, input().split())) for _ in range(19)]
res = game()
print(f'{res[0]}\n{res[1]} {res[2]}' if res else 0)
