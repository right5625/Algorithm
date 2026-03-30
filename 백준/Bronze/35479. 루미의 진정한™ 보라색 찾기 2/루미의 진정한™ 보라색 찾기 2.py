R, G, B = map(int, input().split())
_R, _G, _B = R / 255, G / 255, B / 255
K = 1 - max(_R, _G, _B)
print(f'{(1 - _R - K) / (1 - K)} {(1 - _G - K) / (1 - K)} {(1 - _B - K) / (1 - K)} {K}' if K < 1 else f'0 0 0 1')