k = int(input())
w = int(input())
h = int(input())
t = int(input())
for _ in range(h):
    for _ in range(t):
        print('*' * ((t + k) * w + t))
    for _ in range(k):
        print(''.join(['*' * t + '.' * k for _ in range(w)]) + '*' * t)
for _ in range(t):
    print('*' * ((t + k) * w + t))