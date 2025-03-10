while True:
    S = input()
    if S == '#':
        break
    score1 = score2 = res1 = res2 = 0
    for i in range(len(S)):
        if S[i] == 'A':
            score1 += 1
            if score1 >= 4 and score1 >= score2 + 2:
                res1 += 1
                score1 = score2 = 0
        else:
            score2 += 1
            if score2 >= 4 and score2 >= score1 + 2:
                res2 += 1
                score1 = score2 = 0
    print(f'A {res1} B {res2}')