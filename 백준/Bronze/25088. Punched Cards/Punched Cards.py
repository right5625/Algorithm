for t in range(1, int(input()) + 1):
    R, C = map(int, input().split())
    print(f'Case #{t}:\n..' + '+-' * (C - 1) + '+\n..' + '|.' * (C - 1) + '|')
    for _ in range(R - 1):
        print('+-' * C + '+\n' + '|.' * C + '|')
    print('+-' * C + '+')