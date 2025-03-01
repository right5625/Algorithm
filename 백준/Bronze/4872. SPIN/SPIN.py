N = list(map(int, input()))
size = len(N)
while True:
    try:
        S = list(map(int, input()))
    except:
        break
    for i in range(size):
        N[i] += S[i]
print(''.join(map(lambda x: str(x % 10), N)))