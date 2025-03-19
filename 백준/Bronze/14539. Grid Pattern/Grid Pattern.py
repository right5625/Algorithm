for t in range(1, int(input()) + 1):
    r, c, w, h = map(int, input().split())
    print(f'Case #{t}:')
    for _ in range(r):
        print(('+' + '-' * w) * c + '+')
        for _ in range(h):
            print(('|' + '*' * w) * c + '|')
    print(('+' + '-' * w) * c + '+')