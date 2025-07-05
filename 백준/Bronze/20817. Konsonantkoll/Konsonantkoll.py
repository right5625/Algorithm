prev, cnt = '', 1
result = ''
for i in input():
    if i == prev:
        cnt += 1
    else:
        result += prev * (min(cnt, 2) if prev in 'bcdfghjklmnpqrstvwxz' else cnt)
        cnt = 1
    prev = i
result += prev * min(cnt, 2)
print(result)