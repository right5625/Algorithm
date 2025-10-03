S = int(input())
D = float(input())
T = float(input())
print('MADE IT' if S * 5280 / 3600 * T >= D else 'FAILED TEST')