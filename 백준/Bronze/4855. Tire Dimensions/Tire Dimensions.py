import sys, math

for i in sys.stdin:
    i = i.strip()
    if not i:
        continue
    S = i.split()
    print(f'{i}: {round(math.pi * (((int(S[3]) / 100 * int(S[1]) * 2) + (int(S[-1]) * 25.4)) / 10))}')