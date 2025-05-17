y, m = 2018, 4
lst = []
while y <= 10000:
    lst.append(y)
    y += 2
    m += 2
    if m == 14:
        y += 1
        m = 2
print('yes' if int(input()) in lst else 'no')