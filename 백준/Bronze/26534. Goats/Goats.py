a = list(map(int, input().split()))
b = list(map(int, input().split()))
cnt1, cnt2 = 0, 36
for i in a:
    for j in b:
        if i > j:
            cnt1 += 1
        elif i == j:
            cnt2 -= 1
print(f'{cnt1 / cnt2:.5f}')