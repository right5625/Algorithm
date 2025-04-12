S, N = input().split()
for k, v in {'residential': {1: 0, 5: 1, 10: 2, 15: 3, 20: 4}, 'commercial': {1: 0, 7: 1, 14: 2, 20: 3}, 'industrial': {1: 0, 4: 1, 8: 2, 12: 3, 16: 4, 20: 5}}[S].items():
    if int(N) <= k:
        print(v)
        break