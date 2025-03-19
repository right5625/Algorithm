for t in range(1, int(input()) + 1):
    dic = {}
    for _ in range(int(input())):
        S = input()
        dic[S] = len(set(S.replace(' ', '')))
    print(f'Case #{t}: {sorted(dic.items(), key=lambda x: (-x[1], x[0]))[0][0]}')