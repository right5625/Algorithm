S = input().split()
cnt = 0
for i in S:
    if 'ae' in i:
        cnt += 1
print('dae ae ju traeligt va' if cnt / len(S) >= 0.4 else 'haer talar vi rikssvenska')