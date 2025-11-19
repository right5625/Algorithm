N = int(input())
if N >= 1000000:
    print(int(N * 0.2), int(N * 0.8))
elif N >= 500000:
    print(int(N * 0.15), int(N * 0.85))
elif N >= 100000:
    print(int(N * 0.1), int(N * 0.9))
else:
    print(int(N * 0.05), int(N * 0.95))