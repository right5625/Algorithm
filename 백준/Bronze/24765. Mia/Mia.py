while True:
    s0, s1, r0, r1 = map(int, input().split())
    if s0 == s1 == r0 == r1 == 0:
        break
    s, r = int(''.join(sorted([str(s0), str(s1)], reverse=True))), int(''.join(sorted([str(r0), str(r1)], reverse=True)))
    if s == 21:
        if r == 21:
            print('Tie.')
        else:
            print('Player 1 wins.')
    elif r == 21:
        print('Player 2 wins.')
    elif s in [11, 22, 33, 44, 55, 66]:
        if r in [11, 22, 33, 44, 55, 66]:
            if s > r:
                print('Player 1 wins.')
            elif s < r:
                print('Player 2 wins.')
            else:
                print('Tie.')
        else:
            print('Player 1 wins.')
    elif r in [11, 22, 33, 44, 55, 66]:
        print('Player 2 wins.')
    else:
        if s > r:
            print('Player 1 wins.')
        elif s < r:
            print('Player 2 wins.')
        else:
            print('Tie.')