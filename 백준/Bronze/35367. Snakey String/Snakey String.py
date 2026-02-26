r, c = map(int, input().split())
print(''.join([''.join(i).replace('.', '') for i in list(zip(*[input() for _ in range(r)]))]))