N = int(input())
if N == 1:
    print('*')
else:
    print('*' * N)
    for i in range((N - 2) // 2):
        print('*' + ' ' * i + '*' + ' ' * (N - 4 - i * 2) + '*' + ' ' * i + '*')
    if N % 2 == 1:
        print('*' + ' ' * (N // 2 - 1) + '*' + ' ' * (N // 2 - 1) + '*')
    for i in range((N - 4) // 2, -1, -1):
        print('*' + ' ' * i + '*' + ' ' * (N - 4 - i * 2) + '*' + ' ' * i + '*')
    print('*' * N)