a = list(map(int, input().split()))
print(f'JAH\n{a[0]} {a[1]} {a[1]} {a[0]}' if a[0] == a[3] or a[1] == a[2] else 'EI')
