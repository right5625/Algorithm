h, m, d = input().replace(':',' ').split()
t = int(input())
time = (0 if h == '12' else int(h)) * 60 + int(m) + (720 if d == 'PM' else 0) - t
if time < 0:
    time += 1440
if time >= 720:
    time -= 720
    am_pm = 'PM'
else:
    am_pm = 'AM'
print(f'{time // 60 if time // 60 > 0 else 12}:{time % 60:02d} {am_pm}')