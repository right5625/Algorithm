N, M, S = map(int, input().split())
print(int(min((M + 1) * S * 0.01 * (100 - N), M * S)))