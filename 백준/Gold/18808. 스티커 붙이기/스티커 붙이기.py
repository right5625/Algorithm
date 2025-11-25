N, M, K = map(int, input().split())
notebook = [[0 for _ in range(M)] for _ in range(N)]
for _ in range(K):
    R, C = map(int, input().split())
    sticker = [list(map(int, input().split())) for _ in range(R)]
    attach = False
    for _ in range(4):
        find_start = False
        for sticker_r in range(R):
            for sticker_c in range(C):
                if sticker[sticker_r][sticker_c] == 1:
                    sticker_start_r, sticker_start_c = sticker_r, sticker_c
                    find_start = True
                    break
            if find_start:
                break
        sticker_pos = []
        for sticker_r in range(R):
            for sticker_c in range(C):
                if sticker[sticker_r][sticker_c] == 1:
                    sticker_pos.append([sticker_r, sticker_c])
        for r in range(N):
            for c in range(M):
                if notebook[r][c] == 0:
                    cnt = 0
                    for sticker_r, sticker_c in sticker_pos:
                        mr, mc = r + sticker_r - sticker_start_r, c + sticker_c - sticker_start_c
                        if 0 <= mr < N and 0 <= mc < M and notebook[mr][mc] == 0:
                            cnt += 1
                    if cnt == len(sticker_pos):
                        for sticker_r, sticker_c in sticker_pos:
                            notebook[r + sticker_r - sticker_start_r][c + sticker_c - sticker_start_c] = 1
                        attach = True
                        break
            if attach:
                break
        if attach:
            break
        sticker = [[0 for _ in range(R)] for _ in range(C)]
        for sticker_r, sticker_c in sticker_pos:
            sticker[sticker_c][R - 1 - sticker_r] = 1
        R, C = C, R
print(sum([i.count(1) for i in notebook]))