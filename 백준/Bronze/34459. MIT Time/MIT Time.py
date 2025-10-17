import sys
input = lambda : sys.stdin.readline().rstrip()

for _ in range(int(input())):
    N = int(input())
    k = 1
    while N > 5 ** k:
        k += 1
    print(f'MIT{"" if k == 1 else f"^{k}"} time')