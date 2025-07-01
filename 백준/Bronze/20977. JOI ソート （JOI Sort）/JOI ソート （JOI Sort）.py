N = int(input())
cnt = {'J': 0, 'O': 0, 'I': 0}
for i in input():
    cnt[i] += 1
print(''.join([k * v for k, v in cnt.items()]))