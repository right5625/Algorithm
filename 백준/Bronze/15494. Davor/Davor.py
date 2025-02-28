N = int(input()) // 364
for i in range(100, 0, -1):
    if N - i > 0 and (N - i) % 3 == 0:
        print(f'{i}\n{(N - i) // 3}')
        break