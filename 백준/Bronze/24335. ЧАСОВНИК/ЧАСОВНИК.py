h, m, dh, dm, c = map(int, input().split())
total_minutes = (h * 60 + m) + (dh * 60 + dm)
h, m = divmod(total_minutes, 60)
h %= 12
if c == 1:
    print(f"{h} {m}")
else:
    degree = h * 30 + m * 0.5
    if degree % 6 == 0:
        print(f'@ {int(degree // 6)}')
    else:
        first = int(degree // 6)
        second = (first + 1) % 60
        print(f'{first} {second}')