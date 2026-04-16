while True:
    N, M, P = map(int, input().split())
    if N == M == P == 0:
        break
    total_votes = 0
    winner_votes = 0
    for i in range(1, N + 1):
        X = int(input())
        total_votes += X
        if i == M:
            winner_votes = X
    money = total_votes * (100 - P)
    if winner_votes != 0:
        result = money // winner_votes
    else:
        result = 0
    print(result)